### `BeforeToolSelection`

Fires before the LLM decides which tools to call. Used to filter the available
toolset or force specific tool modes.

- **Input Fields**:
  - `llm_request`: (`object`) Same format as `BeforeModel`.
- **Relevant Output Fields**:
  - `hookSpecificOutput.toolConfig.mode`: (`"AUTO" | "ANY" | "NONE"`)
    - `"NONE"`: Disables all tools (Wins over other hooks).
    - `"ANY"`: Forces at least one tool call.
  - `hookSpecificOutput.toolConfig.allowedFunctionNames`: (`string[]`) Whitelist
    of tool names.
- **Union Strategy**: Multiple hooks' whitelists are **combined**.
- **Limitations**: Does **not** support `decision`, `continue`, or
  `systemMessage`.