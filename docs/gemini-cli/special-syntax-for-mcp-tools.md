### Special syntax for MCP tools

You can create rules that target tools from Model Context Protocol (MCP) servers
using the `mcpName` field. **This is the recommended approach** for defining MCP
policies, as it is much more robust than manually writing Fully Qualified Names
(FQNs) or string wildcards.

<!-- prettier-ignore -->
> [!WARNING]
> Do not use underscores (`_`) in your MCP server names (e.g., use
> `my-server` rather than `my_server`). The policy parser splits Fully Qualified
> Names (`mcp_server_tool`) on the _first_ underscore following the `mcp_`
> prefix. If your server name contains an underscore, the parser will
> misinterpret the server identity, which can cause wildcard rules and security
> policies to fail silently.

**1. Targeting a specific tool on a server**

Combine `mcpName` and `toolName` to target a single operation. When using
`mcpName`, the `toolName` field should strictly be the simple name of the tool
(e.g., `search`), **not** the Fully Qualified Name (e.g., `mcp_server_search`).

```toml