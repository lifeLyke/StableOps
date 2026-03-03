"""LLM wrapper for OpenAI/Anthropic. Returns stub text when API keys are missing."""

import os
from typing import Optional

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
    # Read from environment at call time so Streamlit reloads reflect changes.
    openai_key = os.environ.get("OPENAI_API_KEY")
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")

    if openai_key:
        return _openai_complete(openai_key, system_prompt, user_prompt, model=model or "gpt-4o-mini", max_tokens=max_tokens)
    if anthropic_key:
        return _anthropic_complete(anthropic_key, system_prompt, user_prompt, model=model or "claude-sonnet-4-20250514", max_tokens=max_tokens)
    return _stub_complete(system_prompt, user_prompt)


def _openai_complete(api_key: str, system_prompt: str, user_prompt: str, *, model: str, max_tokens: int) -> str:
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    r = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=max_tokens,
    )
    return (r.choices[0].message.content or "").strip()


def _anthropic_complete(api_key: str, system_prompt: str, user_prompt: str, *, model: str, max_tokens: int) -> str:
    from anthropic import Anthropic
    client = Anthropic(api_key=api_key)
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
