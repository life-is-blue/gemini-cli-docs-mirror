### Conditions

Conditions are the criteria that a tool call must meet for a rule to apply. The
primary conditions are the tool's name and its arguments.

#### Tool Name

The `toolName` in the rule must match the name of the tool being called.

- **Wildcards**: You can use wildcards to match multiple tools.
  - `*`: Matches **any tool** (built-in or MCP).
  - `mcp_server_*`: Matches any tool from a specific MCP server.
  - `mcp_*_toolName`: Matches a specific tool name across **all** MCP servers.
  - `mcp_*`: Matches **any tool from any MCP server**.

> **Recommendation:** While FQN wildcards are supported, the recommended
> approach for MCP tools is to use the `mcpName` field in your TOML rules. See
> [Special syntax for MCP tools](#special-syntax-for-mcp-tools).

#### Arguments pattern

If `argsPattern` is specified, the tool's arguments are converted to a stable
JSON string, which is then tested against the provided regular expression. If
the arguments don't match the pattern, the rule does not apply.

#### Execution environment

If `interactive` is specified, the rule will only apply if the CLI's execution
environment matches the specified boolean value:

- `true`: The rule applies only in interactive mode.
- `false`: The rule applies only in non-interactive (headless) mode.

If omitted, the rule applies to both interactive and non-interactive
environments.