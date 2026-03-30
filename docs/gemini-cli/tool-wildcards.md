### Tool wildcards

When defining `tools` for a subagent, you can use wildcards to quickly grant
access to groups of tools:

- `*`: Grant access to all available built-in and discovered tools.
- `mcp_*`: Grant access to all tools from all connected MCP servers.
- `mcp_my-server_*`: Grant access to all tools from a specific MCP server named
  `my-server`.