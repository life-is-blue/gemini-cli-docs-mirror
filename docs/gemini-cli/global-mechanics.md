### Global mechanics

Understanding these core principles is essential for building robust hooks.

#### Strict JSON requirements (The "Golden Rule")

Hooks communicate via `stdin` (Input) and `stdout` (Output).

1. **Silence is Mandatory**: Your script **must not** print any plain text to
   `stdout` other than the final JSON object. **Even a single `echo` or `print`
   call before the JSON will break parsing.**
2. **Pollution = Failure**: If `stdout` contains non-JSON text, parsing will
   fail. The CLI will default to "Allow" and treat the entire output as a
   `systemMessage`.
3. **Debug via Stderr**: Use `stderr` for **all** logging and debugging (e.g.,
   `echo "debug" >&2`). Gemini CLI captures `stderr` but never attempts to parse
   it as JSON.

#### Exit codes

Gemini CLI uses exit codes to determine the high-level outcome of a hook
execution:

| Exit Code | Label            | Behavioral Impact                                                                                                                                                            |
| --------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0**     | **Success**      | The `stdout` is parsed as JSON. **Preferred code** for all logic, including intentional blocks (e.g., `{"decision": "deny"}`).                                               |
| **2**     | **System Block** | **Critical Block**. The target action (tool, turn, or stop) is aborted. `stderr` is used as the rejection reason. High severity; used for security stops or script failures. |
| **Other** | **Warning**      | Non-fatal failure. A warning is shown, but the interaction proceeds using original parameters.                                                                               |

#### Matchers

You can filter which specific tools or triggers fire your hook using the
`matcher` field.

- **Tool events** (`BeforeTool`, `AfterTool`): Matchers are **Regular
  Expressions**. (e.g., `"write_.*"`).
- **Lifecycle events**: Matchers are **Exact Strings**. (e.g., `"startup"`).
- **Wildcards**: `"*"` or `""` (empty string) matches all occurrences.