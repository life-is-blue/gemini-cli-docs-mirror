### Environment variables

Hooks are executed with a sanitized environment.

- `GEMINI_PROJECT_DIR`: The absolute path to the project root.
- `GEMINI_SESSION_ID`: The unique ID for the current session.
- `GEMINI_CWD`: The current working directory.
- `CLAUDE_PROJECT_DIR`: (Alias) Provided for compatibility.