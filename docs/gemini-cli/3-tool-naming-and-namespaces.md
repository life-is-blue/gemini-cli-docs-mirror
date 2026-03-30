### 3. Tool naming and namespaces

To prevent collisions across multiple servers or conflicting built-in tools,
every discovered MCP tool is assigned a strict namespace.

1. **Automatic FQN:** All MCP tools are unconditionally assigned a fully
   qualified name (FQN) using the format `mcp_{serverName}_{toolName}`.
2. **Registry tracking:** The tool registry maintains metadata mappings between
   these FQNs and their original server identities.
3. **Overwrites:** If two servers share the exact same alias in your
   configuration and provide tools with the exact same name, the last registered
   tool overwrites the previous one.
4. **Policies:** To configure permissions (like auto-approval or denial) for MCP
   tools, see
   [Special syntax for MCP tools](/docs/reference/policy-engine#special-syntax-for-mcp-tools)
   in the Policy Engine documentation.

<!-- prettier-ignore -->
> [!WARNING]
> Do not use underscores (`_`) in your MCP server names (e.g., use
> `my-server` rather than `my_server`). The policy parser splits Fully Qualified
> Names (`mcp_server_tool`) on the _first_ underscore following the `mcp_`
> prefix. If your server name contains an underscore, the parser will
> misinterpret the server identity, which can cause wildcard rules and security
> policies to fail silently.