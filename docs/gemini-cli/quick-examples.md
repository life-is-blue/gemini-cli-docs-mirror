## Quick examples

- One‑off session using a project file:
  - `GEMINI_SYSTEM_MD=1 gemini`
- Persist for a project using `.gemini/.env`:
  - Create `.gemini/system.md`, then add to `.gemini/.env`:
    - `GEMINI_SYSTEM_MD=1`
- Use a custom file under your home directory:
  - `GEMINI_SYSTEM_MD=~/prompts/SYSTEM.md gemini`