### `AfterTool`

Fires after a tool executes. Used for result auditing, context injection, or
hiding sensitive output from the agent.

- **Input Fields**:
  - `tool_name`: (`string`)
  - `tool_input`: (`object`) The original arguments.
  - `tool_response`: (`object`) The result containing `llmContent`,
    `returnDisplay`, and optional `error`.
  - `mcp_context`: (`object`)
  - `original_request_name`: (`string`) The original name of the tool being
    called, if this is a tail tool call.
- **Relevant Output Fields**:
  - `decision`: Set to `"deny"` to hide the real tool output from the agent.
  - `reason`: Required if denied. This text **replaces** the tool result sent
    back to the model.
  - `hookSpecificOutput.additionalContext`: Text that is **appended** to the
    tool result for the agent.
  - `hookSpecificOutput.tailToolCallRequest`: (`{ name: string, args: object }`)
    A request to execute another tool immediately after this one. The result of
    this "tail call" will replace the original tool's response. Ideal for
    programmatic tool routing.
  - `continue`: Set to `false` to **kill the entire agent loop** immediately.
- **Exit Code 2 (Block Result)**: Hides the tool result. Uses `stderr` as the
  replacement content sent to the agent. **The turn continues.**

---