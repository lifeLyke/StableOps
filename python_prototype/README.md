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

Then open the URL shown in the terminal (usually http://localhost:8501).

## API keys (optional)

To get real AI output instead of demo text:

- **OpenAI:** set `OPENAI_API_KEY` in your environment or in a `.env` file in `python_prototype` (use `python-dotenv` in app if you add it).
- **Anthropic:** set `ANTHROPIC_API_KEY` (used if OpenAI is not set).

No keys are required to run the app; templates and stubs are used when keys are missing.

## Project layout

```
python_prototype/
  app.py                 # Streamlit entry
  requirements.txt
  pyproject.toml
  stableops/
    __init__.py
    schemas.py           # Pydantic models (inputs/outputs)
    workflows.py         # Emily workflows (create post, newsletter, grant)
    prompts/             # Prompt templates
      social_post.py
      newsletter.py
      grant.py
    integrations/
      llm.py             # OpenAI/Anthropic wrapper; stub if no key
      email.py           # Stub (send newsletter)
      storage.py         # Local JSON artifacts
  data/                  # Created at runtime for saved artifacts
```

## Copy / download

Each workflow page shows the result and provides:

- **Copy:** use the displayed text area or the download button.
- **Download:** `.txt` for post and newsletter, `.md` for grant draft.

Artifacts are also stored locally under `data/artifacts.json` (or `STABLEOPS_DATA_DIR` if set).
