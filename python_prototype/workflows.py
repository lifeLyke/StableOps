"""Core workflow functions for Emily (StableOps)."""

import json
import logging
import re

from schemas import (
    CreatePostInput,
    CreatePostOutput,
    CreateNewsletterInput,
    CreateNewsletterOutput,
    DraftGrantInput,
    DraftGrantOutput,
    SocialPlatform,
)
from prompts import (
    SOCIAL_POST_SYSTEM,
    SOCIAL_POST_USER,
    NEWSLETTER_SYSTEM,
    NEWSLETTER_USER,
    GRANT_SYSTEM,
    GRANT_USER,
)
from integrations.llm import llm_complete
from config import MAX_TOKENS_GRANT, MAX_TOKENS_NEWSLETTER, MAX_TOKENS_SOCIAL_POST


def run_create_social_post(inp: CreatePostInput, *, use_llm: bool = True) -> CreatePostOutput:
    """
    Create social post content. If use_llm and an API key is set, uses LLM; otherwise
    uses the same template logic as the TS app (Instagram/Facebook blocks).
    """
    if use_llm:
        try:
            user = SOCIAL_POST_USER.format(
                details=inp.details,
                platform=inp.platform.value,
            )
            post_text = llm_complete(SOCIAL_POST_SYSTEM, user, max_tokens=MAX_TOKENS_SOCIAL_POST)
            return CreatePostOutput(post_text=post_text.strip(), platform=inp.platform)
        except Exception as e:
            logging.exception("LLM call failed for social post, using template fallback: %s", e)
    # Fallback when LLM is not available
    post = ""
    if inp.platform in (SocialPlatform.INSTAGRAM, SocialPlatform.BOTH):
        post += f"🐴 {inp.details}\n\nJoin us and be part of something special! ❤️\n\n#therapeuticriding #horses #community #nonprofit\n\n"
    if inp.platform in (SocialPlatform.FACEBOOK, SocialPlatform.BOTH):
        post += f"We're excited to share some news from our farm!\n\n{inp.details}\n\nWe'd love to see you there. Tag a friend who would enjoy this! 🐎"
    return CreatePostOutput(post_text=post.strip(), platform=inp.platform)


def run_create_newsletter(inp: CreateNewsletterInput) -> CreateNewsletterOutput:
    """Generate newsletter subject and body using LLM (or stub)."""
    user = NEWSLETTER_USER.format(
        topic=inp.topic,
        highlights=inp.highlights or "(none specified)",
        tone=inp.tone,
    )
    raw = llm_complete(NEWSLETTER_SYSTEM, user, max_tokens=MAX_TOKENS_NEWSLETTER)
    subject_line = "Newsletter from StableOps"
    body_plain = raw
    # Try to parse JSON; strip markdown code fence if present
    text = raw.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        text = match.group(1).strip()
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            subject_line = parsed.get("subject", subject_line) or subject_line
            body_plain = parsed.get("body", raw) or raw
    except (json.JSONDecodeError, TypeError):
        pass
    return CreateNewsletterOutput(
        subject_line=subject_line,
        body_plain=body_plain,
        body_html="",
    )


def run_draft_grant_proposal(inp: DraftGrantInput) -> DraftGrantOutput:
    """Draft grant proposal sections using LLM (or stub)."""
    user = GRANT_USER.format(
        program_name=inp.program_name,
        amount_requested=inp.amount_requested,
        purpose=inp.purpose,
        audience=inp.audience or "(not specified)",
        deadline=inp.deadline or "(not specified)",
    )
    draft_sections = llm_complete(GRANT_SYSTEM, user, max_tokens=MAX_TOKENS_GRANT)
    # Simple heading extraction: lines that look like section titles (short, end with : or all-caps)
    suggested_headings = []
    for line in draft_sections.split("\n"):
        s = line.strip().rstrip(":")
        if s and len(s) < 80 and (line.strip().endswith(":") or (len(s) > 2 and s.isupper() and len(s) < 50)):
            suggested_headings.append(s)
    suggested_headings = suggested_headings[:10]
    return DraftGrantOutput(
        draft_sections=draft_sections,
        suggested_headings=suggested_headings or ["Need Statement", "Program Description", "Goals", "Budget Narrative"],
    )
