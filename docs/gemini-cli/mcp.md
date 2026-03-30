### `/mcp`

- **Description:** Manage configured Model Context Protocol (MCP) servers.
- **Sub-commands:**
  - **`auth`**:
    - **Description:** Authenticate with an OAuth-enabled MCP server.
    - **Usage:** `/mcp auth <server-name>`
    - **Details:** If `<server-name>` is provided, it initiates the OAuth flow
      for that server. If no server name is provided, it lists all configured
      servers that support OAuth authentication.
  - **`desc`**
    - **Description:** List configured MCP servers and tools with descriptions.
  - **`disable`**
    - **Description:** Disable an MCP server.
  - **`enable`**
    - **Description:** Enable a disabled MCP server.
  - **`list`** or **`ls`**:
    - **Description:** List configured MCP servers and tools. This is the
      default action if no subcommand is specified.
  - **`reload`**:
    - **Description:** Reloads all MCP servers and re-discovers their available
      tools.
  - **`schema`**:
    - **Description:** List configured MCP servers and tools with descriptions
      and schemas.