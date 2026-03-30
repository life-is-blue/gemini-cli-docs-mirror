### Configure the MCP server in settings.json

You can configure MCP servers in your `settings.json` file in two main ways:
through the top-level `mcpServers` object for specific server definitions, and
through the `mcp` object for global settings that control server discovery and
execution.

#### Global MCP settings (`mcp`)

The `mcp` object in your `settings.json` lets you define global rules for all
MCP servers.

- **`mcp.serverCommand`** (string): A global command to start an MCP server.
- **`mcp.allowed`** (array of strings): A list of MCP server names to allow. If
  this is set, only servers from this list (matching the keys in the
  `mcpServers` object) will be connected to.
- **`mcp.excluded`** (array of strings): A list of MCP server names to exclude.
  Servers in this list will not be connected to.

**Example:**

```json
{
  "mcp": {
    "allowed": ["my-trusted-server"],
    "excluded": ["experimental-server"]
  }
}
```

#### Server-specific configuration (`mcpServers`)

The `mcpServers` object is where you define each individual MCP server you want
the CLI to connect to.