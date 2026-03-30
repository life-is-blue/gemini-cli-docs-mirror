## Export the default prompt (recommended)

Before overriding, export the current default prompt so you can review required
safety and workflow rules.

- Write the built‑in prompt to the project default path:
  - `GEMINI_WRITE_SYSTEM_MD=1 gemini`
- Or write to a custom path:
  - `GEMINI_WRITE_SYSTEM_MD=~/prompts/DEFAULT_SYSTEM.md gemini`

This creates the file and writes the current built‑in system prompt to it.