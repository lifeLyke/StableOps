"""Prompts for Create Newsletter workflow."""

NEWSLETTER_SYSTEM = """You are writing a newsletter for a therapeutic riding nonprofit.
Write a warm, professional email that highlights program news, events, and impact.
Include a compelling subject line and a clear call to action. Keep paragraphs short."""

NEWSLETTER_USER = """Draft a newsletter with:

Topic: {topic}
Highlights to include: {highlights}
Tone: {tone}

Provide:
1. Subject line (one line)
2. Body (plain text, suitable for email). Use clear section headings if needed."""
