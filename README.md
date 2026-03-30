# Gemini CLI Docs Mirror

Local mirror for Gemini CLI documentation, designed for automation-first ingestion.

This repository fetches the complete Gemini CLI documentation and stores it locally for indexing/analysis workflows.

## Source

- `https://geminicli.com/llms.txt` - Gemini CLI documentation (all-in-one format)

## Layout

- `scripts/fetch_gemini_docs.py`: fetcher + manifest generator
- `config/sources.json`: source definitions
- `docs/`: mirrored markdown content and manifest
- `.cnb.yml`: CNB scheduled + manual sync workflow
- `.cnb/web_trigger.yml`: CNB page button configuration

## Run locally

```bash
pip install -r scripts/requirements.txt
python3 scripts/fetch_gemini_docs.py
```

## CNB automation

This repository is configured for CNB-native automation:

- Scheduled sync every 6 hours
- Manual sync button on `main` branch page
- Push / PR validation on fetcher changes

## Notes

- Source content remains property of Google.
- This repository stores mirrored copies for internal indexing/analysis workflows.
