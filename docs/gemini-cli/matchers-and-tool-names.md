### Matchers and tool names

For `BeforeTool` and `AfterTool` events, the `matcher` field in your settings is
compared against the name of the tool being executed.

- **Built-in Tools**: You can match any built-in tool (e.g., `read_file`,
  `run_shell_command`). See the [Tools Reference](/docs/reference/tools) for a full
  list of available tool names.
- **MCP Tools**: Tools from MCP servers follow the naming pattern
  `mcp_<server_name>_<tool_name>`.
- **Regex Support**: Matchers support regular expressions (e.g.,
  `matcher: "read_.*"` matches all file reading tools).