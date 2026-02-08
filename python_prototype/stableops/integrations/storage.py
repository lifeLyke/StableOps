"""Local storage for artifacts (generated posts, drafts). Uses JSON in a local folder."""

import json
import os
from pathlib import Path
from typing import Any

# Default: store under python_prototype/data (or cwd/data)
DATA_DIR = Path(os.environ.get("STABLEOPS_DATA_DIR", Path(__file__).resolve().parent.parent.parent / "data"))
ARTIFACTS_FILE = DATA_DIR / "artifacts.json"


def _ensure_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def _load() -> list[dict[str, Any]]:
    _ensure_dir()
    if not ARTIFACTS_FILE.exists():
        return []
    try:
        with open(ARTIFACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def _save(records: list[dict[str, Any]]) -> None:
    _ensure_dir()
    with open(ARTIFACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)


def save_artifact(kind: str, content: str, meta: dict[str, Any] | None = None) -> str:
    """Append an artifact (e.g. 'social_post', 'newsletter', 'grant_draft'). Returns an id."""
    import uuid
    records = _load()
    id_ = str(uuid.uuid4())[:8]
    records.append({
        "id": id_,
        "kind": kind,
        "content": content,
        "meta": meta or {},
    })
    _save(records)
    return id_


def load_artifacts(kind: str | None = None, limit: int = 50) -> list[dict[str, Any]]:
    """Load recent artifacts, optionally filtered by kind. Newest first."""
    records = _load()
    if kind:
        records = [r for r in records if r.get("kind") == kind]
    return list(reversed(records[-limit:]))
