"""Central configuration from environment with sensible defaults."""

import os
from pathlib import Path

_ROOT = Path(__file__).resolve().parent

# LLM API keys (no defaults)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

# Default models
DEFAULT_OPENAI_MODEL = os.environ.get("STABLEOPS_OPENAI_MODEL", "gpt-4o-mini")
DEFAULT_ANTHROPIC_MODEL = os.environ.get("STABLEOPS_ANTHROPIC_MODEL", "claude-3-haiku-20240307")

# Data directory for artifacts
_DATA_DIR_STR = os.environ.get("STABLEOPS_DATA_DIR")
DATA_DIR = Path(_DATA_DIR_STR) if _DATA_DIR_STR else _ROOT / "data"

# Per-workflow max tokens (optional overrides via env)
MAX_TOKENS_SOCIAL_POST = int(os.environ.get("STABLEOPS_MAX_TOKENS_SOCIAL_POST", "512"))
MAX_TOKENS_NEWSLETTER = int(os.environ.get("STABLEOPS_MAX_TOKENS_NEWSLETTER", "1024"))
MAX_TOKENS_GRANT = int(os.environ.get("STABLEOPS_MAX_TOKENS_GRANT", "2048"))
