## Controlling network access via proxy

In corporate environments with strict network policies, you can configure Gemini
CLI to route all outbound traffic through a corporate proxy. This can be set via
an environment variable, but it can also be enforced for custom tools via the
`mcpServers` configuration.

**Example (for an MCP server):**

```json
{
  "mcpServers": {
    "proxied-server": {
      "command": "node",
      "args": ["mcp_server.js"],
      "env": {
        "HTTP_PROXY": "http://proxy.example.com:8080",
        "HTTPS_PROXY": "http://proxy.example.com:8080"
      }
    }
  }
}
```