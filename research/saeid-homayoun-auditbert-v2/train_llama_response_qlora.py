#!/usr/bin/env python3
"""Independent, private QLoRA KAM audit-response SFT research track.

Requires a GPU runtime, acceptance of the Meta Llama 3.1 license, and explicit
rights to use all training text. This is research code, NOT trained weights.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd
from train_finbert_topic import prepare_table, holdouts


def prepare_responses(path: Path):
    data, report = prepare_table(path)
    if "response" not in data:
        raise ValueError("A separately sourced and licensed 'response' column is required.")
    data = data.dropna(subset=["response"]).copy()
    data["response"] = data["response"].astype(str).str.strip()
    data = data[data["response"].str.len() >= 25].reset_index(drop=True)
    if len(data) < 3:
        raise ValueError("Too few response-labeled records.")
    report["response_rows"] = int(len(data))
    report["response_source_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    return data, report


def conversation_pairs(df):
    """Prompt-completion dataset; completion-only labels prevent copying prompts."""
    def make_prompt(row):
        return [
            {"role": "system", "content":
                "You are drafting a research illustration of an auditor's response to "
                "a CAM/KAM. Ground text ONLY in the supplied matter; never assert "
                "procedures actually occurred without independent audit evidence. "
                "Flag missing evidence. Not an audit opinion."},
            {"role": "user", "content":
                "Accounting topic: " + str(row["topic"]) +
                "\nMatter title: " + str(row["title"]) +
                "\nDisclosure: " + str(row["description"]) +
                "\nDraft a cautious illustrative audit response based solely "
                "on evidence provided above."}
        ]
    return [{
        "prompt": make_prompt(row),
        "completion": [{"role": "assistant", "content": row["response"]}],
    } for _, row in df.iterrows()]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path, default=Path("private_auditbert_v2_qlora"))
    p.add_argument("--base-model", default="meta-llama/Llama-3.1-8B-Instruct")
    p.add_argument("--split", choices=("company", "year"), default="company")
    p.add_argument("--cutoff", type=int)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--epochs", type=float, default=1)
    p.add_argument("--max-length", type=int, default=1024)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    df, report = prepare_responses(args.input)
    if args.dry_run:
        print(json.dumps({
            "status": "SCHEMA_ONLY_NOT_TRAINED", "response_rows": report["response_rows"],
            "source_sha256": report["response_source_sha256"]}, indent=2))
        return
    train, val, test = holdouts(df, args.split, args.cutoff, args.seed)
    import torch
    if not torch.cuda.is_available():
        raise RuntimeError("QLoRA 8B training requires CUDA GPU: use Colab/Kaggle GPU runtime.")
    from datasets import Dataset
    from peft import LoraConfig, prepare_model_for_kbit_training
    from transformers import (
        AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, set_seed,
    )
    from trl import SFTConfig, SFTTrainer

    set_seed(args.seed)
    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    quant = BitsAndBytesConfig(
        load_in_4bit=True, bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=dtype,
    )
    tokenizer = AutoTokenizer.from_pretrained(args.base_model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        args.base_model, quantization_config=quant, device_map="auto"
    )
    model.config.use_cache = False
    model = prepare_model_for_kbit_training(model)
    lora = LoraConfig(
        r=16, lora_alpha=32, lora_dropout=0.05, bias="none",
        task_type="CAUSAL_LM",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                        "gate_proj", "up_proj", "down_proj"],
    )
    args.output.mkdir(parents=True, exist_ok=True)
    cfg = SFTConfig(
        output_dir=str(args.output / "checkpoints"),
        num_train_epochs=args.epochs,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=8,
        learning_rate=2e-4,
        max_length=args.max_length,
        completion_only_loss=True,
        eval_strategy="epoch", save_strategy="epoch",
        save_total_limit=2, report_to="none", seed=args.seed,
        fp16=dtype == torch.float16, bf16=dtype == torch.bfloat16,
        gradient_checkpointing=True, packing=False,
    )
    trainer = SFTTrainer(
        model=model, args=cfg, processing_class=tokenizer,
        train_dataset=Dataset.from_list(conversation_pairs(train)),
        eval_dataset=Dataset.from_list(conversation_pairs(val)),
        peft_config=lora,
    )
    trainer.train()
    # Test dataset only measured once after training; this loss is NOT BERTScore.
    loss_metrics = trainer.evaluate(
        eval_dataset=Dataset.from_list(conversation_pairs(test)),
        metric_key_prefix="heldout"
    )
    trainer.save_model(str(args.output / "adapter"))
    tokenizer.save_pretrained(str(args.output / "adapter"))
    report.update({
        "status": "SFT_ADAPTER_TRAINED_NOT_HUMAN_AUDITED",
        "base_model": args.base_model, "seed": args.seed,
        "split_method": args.split, "year_cutoff": args.cutoff,
        "split_rows": {"train": len(train), "validation": len(val), "test": len(test)},
        "heldout_loss_only": {k: float(v) for k, v in loss_metrics.items()
                              if isinstance(v, (int, float))},
        "bert_score_f1": None, "auditor_evaluation": None,
        "note": "No generation quality, accuracy or disclosure-specificity metric "
                "is established by evaluation loss."
    })
    (args.output / "experiment_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({
        "status": report["status"], "heldout_loss_only": report["heldout_loss_only"]
    }, indent=2))


if __name__ == "__main__":
    main()
