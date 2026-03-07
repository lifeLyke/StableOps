# StableOps Python Prototype

Python prototype of the StableOps app: **business logic and AI workflows only** (no Expo/React Native UI). Built for user validation with Emily.

## What’s included

- **Create Social Post** — Same behavior as the TS app (template or optional LLM); platform: Instagram / Facebook / Both.
- **Create Newsletter** — AI-generated subject line and body (LLM or demo stub).
- **Draft Grant Proposal** — AI-generated grant narrative sections (LLM or demo stub).

Integrations (LLM, email, storage) are stubbed when credentials are missing so you can run and demo without API keys.

## How to run

From the **repository root** (`StableOps`):

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r python_prototype/requirements.txt
streamlit run python_prototype/app.py
```

Or from **inside** `python_prototype`:

```bash
cd python_prototype
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

If `python` or `pip` is not found, use `python3` and `python3 -m pip` instead. Create the venv on the same OS you run on (e.g. do not reuse a Windows `.venv` on WSL/Linux).

Then open the URL shown in the terminal (usually http://localhost:8501).

## Configuration

All configuration is read from the environment (or a `.env` file in `python_prototype`; the app loads it via `python-dotenv`). See [config.py](config.py) for the source.

**API keys (optional)** — To get real AI output instead of demo text:

- `OPENAI_API_KEY` — OpenAI (used first if set).
- `ANTHROPIC_API_KEY` — Anthropic (used if OpenAI is not set).

No keys are required; templates and stubs are used when keys are missing.

**Optional overrides:**

- `STABLEOPS_DATA_DIR` — Directory for artifacts (default: `python_prototype/data`).
- `STABLEOPS_OPENAI_MODEL` — Default OpenAI model (e.g. `gpt-4o-mini`).
- `STABLEOPS_ANTHROPIC_MODEL` — Default Anthropic model (e.g. `claude-3-haiku-20240307`).
- `STABLEOPS_MAX_TOKENS_SOCIAL_POST`, `STABLEOPS_MAX_TOKENS_NEWSLETTER`, `STABLEOPS_MAX_TOKENS_GRANT` — Max tokens per workflow (defaults: 512, 1024, 2048).

## Project layout

```
python_prototype/
  app.py                 # Streamlit entry
  config.py              # Central config (env: API keys, models, DATA_DIR, max_tokens)
  schemas.py             # Pydantic models (inputs/outputs)
  workflows.py           # Emily workflows (create post, newsletter, grant)
  prompts/               # Prompt templates
    social_post.py
    newsletter.py
    grant.py
  integrations/
    llm.py               # OpenAI/Anthropic wrapper; stub if no key
    email.py             # Stub (send newsletter; reserved for future use)
    storage.py           # Local JSON artifacts
  requirements.txt
  pyproject.toml
  data/                  # Created at runtime for saved artifacts
```

## Copy / download

Each workflow page shows the result and provides:

- **Copy:** use the displayed text area or the download button.
- **Download:** `.txt` for post and newsletter, `.md` for grant draft.

Artifacts are also stored locally under `data/artifacts.json` (or `STABLEOPS_DATA_DIR` if set).
