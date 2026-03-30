### `SessionStart`

Fires on application startup, resuming a session, or after a `/clear` command.
Used for loading initial context.

- **Input fields**:
  - `source`: (`"startup" | "resume" | "clear"`)
- **Relevant output fields**:
  - `hookSpecificOutput.additionalContext`: (`string`)
    - **Interactive**: Injected as the first turn in history.
    - **Non-interactive**: Prepended to the user's prompt.
  - `systemMessage`: Shown at the start of the session.
- **Advisory only**: `continue` and `decision` fields are **ignored**. Startup
  is never blocked.