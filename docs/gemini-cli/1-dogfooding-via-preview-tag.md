### 1. Dogfooding via `preview` tag

The weekly release cadence promotes code from `main` -> `nightly` -> `preview`
-> `stable`.

- **Requirement:** The `preview` release must be used by maintainers for at
  least **one week** before being promoted to `stable`.
- **Action:** Maintainers should install the preview version locally:
  ```bash
  npm install -g @google/gemini-cli@preview
  ```
- **Goal:** To catch regressions and UX issues in day-to-day usage before they
  reach the broad user base.