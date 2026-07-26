# CLI Docs Mirror

Local mirror for official CLI Markdown docs (Gemini CLI and Cursor CLI).

## Open-Source Positioning

This repository is an open mirror of publicly available CLI documentation,
designed to make agent-oriented document ingestion and retrieval easier.

- Canonical sources remain the official docs sites.
- This mirror does not redefine or replace official documentation.
- We only mirror documentation discovered from official `llms.txt` indexes.
- Each mirrored file keeps source metadata (`url`, `sha256`, `fetched_at`) in `docs/docs_manifest.json`.

This repository is designed for automation-first ingestion:
- Periodically fetches `llms.txt` indexes from configured sources
- Resolves linked docs Markdown pages
- Stores mirrored files under `docs/`
- Writes `docs/docs_manifest.json` with hashes and source metadata

## Sources

Configured in `config/sources.json`:
- `https://geminicli.com/llms.txt` → `docs/gemini-cli/`
- `https://cursor.com/llms.txt` (CLI paths only: `/docs/cli/`) → `docs/cursor-cli/`

## Layout

- `scripts/fetch_docs.py`: fetcher + manifest generator
- `scripts/fetch_gemini_docs.py`: backward-compatible wrapper
- `config/sources.json`: source definitions
- `docs/`: mirrored markdown content and manifest
- `.cnb.yml`: CNB scheduled + manual sync workflow
- `.cnb/web_trigger.yml`: CNB page button configuration

## Run locally

```bash
pip install -r scripts/requirements.txt
python3 scripts/fetch_docs.py
```

Optional strict mode:

```bash
STRICT_FETCH=1 python3 scripts/fetch_docs.py
```

## Automation

This repository supports both CNB and GitHub Actions automation:

- CNB scheduled sync daily: `main -> "crontab: 0 0 * * *"`
- CNB manual sync button on `main` branch page: **Sync CLI Docs**
- GitHub Actions scheduled sync daily: `.github/workflows/update-docs.yml`
- Push / PR validation on `main` for fetcher changes (`scripts/**`, `config/**`, `.cnb.yml`, `.cnb/web_trigger.yml`)

## Notes

- Gemini CLI source content remains property of Google.
- Cursor CLI source content remains property of Anysphere / Cursor.
- This repository stores mirrored copies to support machine-readable indexing and agent retrieval workflows.
- Official docs should always be treated as the source of truth when discrepancies appear.

## Roadmap

1. Keep a stable daily sync baseline.
2. Preserve manual sync triggers for urgent refreshes.
3. Add retrieval-focused artifacts (diff summaries / normalized indexes) to improve agent read quality.
4. Keep CNB and GitHub Actions workflows aligned with the same daily sync policy.
