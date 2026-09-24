"""Minimal Phase-4 HTTP adapters.

No provider SDK is required. Exact model IDs and non-default endpoints are
supplied through environment variables so the scientific record can freeze
the actual provider/model/API version used for each run.
"""

from __future__ import annotations

import json
import os
from urllib.request import Request, urlopen


def post_json(url: str, headers: dict[str, str], payload: dict) -> dict:
    req = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )
    with urlopen(req, timeout=120) as response:
        return json.load(response)


def call_openai_compatible(cfg: dict, prompt: str) -> str:
    key = os.environ[cfg["api_key_env"]]
    model = os.environ[cfg["model_env"]]
    url = os.environ.get(cfg["url_env"]) or cfg.get("default_url")
    if not url:
        raise RuntimeError(f"Missing endpoint env {cfg['url_env']}")
    header_name = cfg.get("api_key_header", "Authorization")
    headers = (
        {header_name: key}
        if header_name != "Authorization"
        else {"Authorization": f"Bearer {key}"}
    )
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Return only valid JSON. Do not add markdown."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0,
    }
    result = post_json(url, headers, payload)
    return result["choices"][0]["message"]["content"]


def call_anthropic(cfg: dict, prompt: str) -> str:
    key = os.environ[cfg["api_key_env"]]
    model = os.environ[cfg["model_env"]]
    url = os.environ.get(cfg["url_env"]) or cfg.get("default_url")
    if not url:
        raise RuntimeError(f"Missing endpoint env {cfg['url_env']}")
    result = post_json(
        url,
        {
            "x-api-key": key,
            "anthropic-version": os.environ.get("ANTHROPIC_VERSION", "2023-06-01"),
        },
        {
            "model": model,
            "max_tokens": 1200,
            "temperature": 0,
            "system": "Return only valid JSON. Do not add markdown.",
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    return "".join(x.get("text", "") for x in result.get("content", []) if x.get("type") == "text")


def call_gemini(cfg: dict, prompt: str) -> str:
    key = os.environ[cfg["api_key_env"]]
    model = os.environ[cfg["model_env"]]
    url = os.environ.get(cfg["url_env"])
    if not url:
        raise RuntimeError(
            "Set GEMINI_GENERATE_CONTENT_URL to the exact generateContent endpoint "
            "for the model/API version under test."
        )
    separator = "&" if "?" in url else "?"
    if "key=" not in url:
        url = f"{url}{separator}key={key}"
    result = post_json(
        url,
        {},
        {
            "contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0},
        },
    )
    parts = result["candidates"][0]["content"]["parts"]
    return "".join(part.get("text", "") for part in parts)


def call_provider(cfg: dict, prompt: str) -> str:
    transport = cfg["transport"]
    if transport == "openai_compatible":
        return call_openai_compatible(cfg, prompt)
    if transport == "anthropic_messages":
        return call_anthropic(cfg, prompt)
    if transport == "gemini_generate_content":
        return call_gemini(cfg, prompt)
    raise RuntimeError(f"Unsupported transport: {transport}")
