## Global hook mechanics

- **Communication**: `stdin` for Input (JSON), `stdout` for Output (JSON), and
  `stderr` for logs and feedback.
- **Exit codes**:
  - `0`: Success. `stdout` is parsed as JSON. **Preferred for all logic.**
  - `2`: System Block. The action is blocked; `stderr` is used as the rejection
    reason.
  - `Other`: Warning. A non-fatal failure occurred; the CLI continues with a
    warning.
- **Silence is Mandatory**: Your script **must not** print any plain text to
  `stdout` other than the final JSON.

---