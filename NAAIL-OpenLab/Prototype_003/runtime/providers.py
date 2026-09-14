from __future__ import annotations

from dataclasses import dataclass
import json
import os
from typing import Any, Dict


class ProviderConfigurationError(RuntimeError):
    pass


class ProviderResponseError(RuntimeError):
    pass


def _extract_json(text: str) -> Dict[str, Any]:
    cleaned = (text or "").strip()
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()
        if cleaned.startswith("json"):
            cleaned = cleaned[4:].lstrip()
    try:
        value = json.loads(cleaned)
    except json.JSONDecodeError:
        start = cleaned.find("{")
        end = cleaned.rfind("}")
        if start < 0 or end <= start:
            raise ProviderResponseError("Provider response did not contain a JSON object.")
        try:
            value = json.loads(cleaned[start : end + 1])
        except json.JSONDecodeError as exc:
            raise ProviderResponseError("Provider JSON could not be parsed.") from exc
    if not isinstance(value, dict):
        raise ProviderResponseError("Provider response must be a JSON object.")
    return value


@dataclass
class ProviderInfo:
    provider: str
    model: str


class BaseProvider:
    info: ProviderInfo

    def generate_json(self, system: str, user: str) -> Dict[str, Any]:
        raise NotImplementedError


class GeminiProvider(BaseProvider):
    def __init__(self, api_key: str | None = None, model: str | None = None):
        key = api_key or os.getenv("GEMINI_API_KEY")
        if not key:
            raise ProviderConfigurationError("GEMINI_API_KEY is not configured.")
        self.info = ProviderInfo(
            provider="google_gemini",
            model=model or os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        )
        try:
            from google import genai
            from google.genai import types
        except ImportError as exc:
            raise ProviderConfigurationError(
                "Install provider dependencies with: pip install -r requirements-providers.txt"
            ) from exc
        self._types = types
        self._client = genai.Client(api_key=key)

    def generate_json(self, system: str, user: str) -> Dict[str, Any]:
        config = self._types.GenerateContentConfig(
            system_instruction=system,
            response_mime_type="application/json",
            temperature=0,
        )
        response = self._client.models.generate_content(
            model=self.info.model,
            contents=user,
            config=config,
        )
        return _extract_json(response.text or "")


class FoundryProvider(BaseProvider):
    def __init__(
        self,
        endpoint: str | None = None,
        credential: str | None = None,
        model: str | None = None,
    ):
        endpoint = endpoint or os.getenv("AZURE_INFERENCE_ENDPOINT")
        credential = credential or os.getenv("AZURE_INFERENCE_CREDENTIAL")
        model = model or os.getenv("AZURE_INFERENCE_MODEL")
        missing = [
            name
            for name, value in (
                ("AZURE_INFERENCE_ENDPOINT", endpoint),
                ("AZURE_INFERENCE_CREDENTIAL", credential),
                ("AZURE_INFERENCE_MODEL", model),
            )
            if not value
        ]
        if missing:
            raise ProviderConfigurationError(
                "Missing Microsoft Foundry configuration: " + ", ".join(missing)
            )
        try:
            from azure.ai.inference import ChatCompletionsClient
            from azure.ai.inference.models import SystemMessage, UserMessage
            from azure.core.credentials import AzureKeyCredential
        except ImportError as exc:
            raise ProviderConfigurationError(
                "Install provider dependencies with: pip install -r requirements-providers.txt"
            ) from exc
        self.info = ProviderInfo(provider="microsoft_foundry", model=str(model))
        self._SystemMessage = SystemMessage
        self._UserMessage = UserMessage
        self._client = ChatCompletionsClient(
            endpoint=str(endpoint),
            credential=AzureKeyCredential(str(credential)),
        )

    def generate_json(self, system: str, user: str) -> Dict[str, Any]:
        response = self._client.complete(
            messages=[
                self._SystemMessage(content=system),
                self._UserMessage(content=user),
            ],
            model=self.info.model,
            temperature=0,
        )
        text = response.choices[0].message.content
        return _extract_json(text or "")


def build_provider(name: str) -> BaseProvider:
    normalized = name.strip().lower()
    if normalized in {"gemini", "google", "google_gemini"}:
        return GeminiProvider()
    if normalized in {"foundry", "microsoft", "microsoft_foundry", "azure"}:
        return FoundryProvider()
    raise ProviderConfigurationError(f"Unsupported provider: {name}")
