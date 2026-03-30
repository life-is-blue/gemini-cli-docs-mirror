### `SessionEnd`

Fires when the CLI exits or a session is cleared. Used for cleanup or final
telemetry.

- **Input Fields**:
  - `reason`: (`"exit" | "clear" | "logout" | "prompt_input_exit" | "other"`)
- **Relevant Output Fields**:
  - `systemMessage`: Displayed to the user during shutdown.
- **Best Effort**: The CLI **will not wait** for this hook to complete and
  ignores all flow-control fields (`continue`, `decision`).