## How to enable

You can set the environment variable temporarily in your shell, or persist it
via a `.gemini/.env` file. See
[Persisting Environment Variables](/docs/get-started/authentication#persisting-environment-variables).

- Use the project default path (`.gemini/system.md`):
  - `GEMINI_SYSTEM_MD=true` or `GEMINI_SYSTEM_MD=1`
  - The CLI reads `./.gemini/system.md` (relative to your current project
    directory).

- Use a custom file path:
  - `GEMINI_SYSTEM_MD=/absolute/path/to/my-system.md`
  - Relative paths are supported and resolved from the current working
    directory.
  - Tilde expansion is supported (e.g., `~/my-system.md`).

- Disable the override (use built‑in prompt):
  - `GEMINI_SYSTEM_MD=false` or `GEMINI_SYSTEM_MD=0` or unset the variable.

If the override is enabled but the target file does not exist, the CLI will
error with: `missing system prompt file '<path>'`.