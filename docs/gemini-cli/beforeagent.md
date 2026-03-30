### `BeforeAgent`

Fires after a user submits a prompt, but before the agent begins planning. Used
for prompt validation or injecting dynamic context.

- **Input Fields**:
  - `prompt`: (`string`) The original text submitted by the user.
- **Relevant Output Fields**:
  - `hookSpecificOutput.additionalContext`: Text that is **appended** to the
    prompt for this turn only.
  - `decision`: Set to `"deny"` to block the turn and **discard the user's
    message** (it will not appear in history).
  - `continue`: Set to `false` to block the turn but **save the message to
    history**.
  - `reason`: Required if denied or stopped.
- **Exit Code 2 (Block Turn)**: Aborts the turn and erases the prompt from
  context. Same as `decision: "deny"`.