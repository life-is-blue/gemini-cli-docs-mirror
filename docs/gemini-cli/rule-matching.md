## Rule matching

When a tool call is made, the engine checks it against all active rules,
starting from the highest priority. The first rule that matches determines the
outcome.

A rule matches a tool call if all of its conditions are met:

1.  **Tool name**: The `toolName` in the rule must match the name of the tool
    being called.
    - **Wildcards**: You can use wildcards like `*`, `mcp_server_*`, or
      `mcp_*_toolName` to match multiple tools. See [Tool Name](#tool-name) for
      details.
2.  **Arguments pattern**: If `argsPattern` is specified, the tool's arguments
    are converted to a stable JSON string, which is then tested against the
    provided regular expression. If the arguments don't match the pattern, the
    rule does not apply.