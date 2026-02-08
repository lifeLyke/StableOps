"""Integrations for LLM, email, and storage (stubbed when credentials missing)."""

from .llm import llm_complete
from .email import send_newsletter  # noqa: F401
from .storage import save_artifact, load_artifacts  # noqa: F401

__all__ = ["llm_complete", "send_newsletter", "save_artifact", "load_artifacts"]
