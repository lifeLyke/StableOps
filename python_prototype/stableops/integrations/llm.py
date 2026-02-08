"""LLM wrapper for OpenAI/Anthropic. Returns stub text when API keys are missing."""

import os
from typing import Optional

# Prefer OpenAI if key is set; otherwise Anthropic; otherwise stub
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY")


def llm_complete(
    system_prompt: str,
    user_prompt: str,
    *,
    model: Optional[str] = None,
    max_tokens: int = 1024,
) -> str:
    """
    Run one completion. Uses OpenAI if OPENAI_API_KEY is set, else Anthropic if set, else stub.
    """
    if OPENAI_KEY:
        return _openai_complete(system_prompt, user_prompt, model=model or "gpt-4o-mini", max_tokens=max_tokens)
    if ANTHROPIC_KEY:
        return _anthropic_complete(system_prompt, user_prompt, model=model or "claude-3-haiku-20240307", max_tokens=max_tokens)
    return _stub_complete(system_prompt, user_prompt)


def _openai_complete(system_prompt: str, user_prompt: str, *, model: str, max_tokens: int) -> str:
    from openai import OpenAI
    client = OpenAI(api_key=OPENAI_KEY)
    r = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=max_tokens,
    )
    return (r.choices[0].message.content or "").strip()


def _anthropic_complete(system_prompt: str, user_prompt: str, *, model: str, max_tokens: int) -> str:
    from anthropic import Anthropic
    client = Anthropic(api_key=ANTHROPIC_KEY)
    r = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return (r.content[0].text if r.content else "").strip()


def _stub_complete(system_prompt: str, user_prompt: str) -> str:
    """Return placeholder when no API key is configured (for demo without credentials)."""
    return (
        "[Demo mode — no API key set]\n\n"
        "Set OPENAI_API_KEY or ANTHROPIC_API_KEY in your environment (or .env) to get real AI output.\n\n"
        "User request was:\n" + user_prompt[:500]
    )
