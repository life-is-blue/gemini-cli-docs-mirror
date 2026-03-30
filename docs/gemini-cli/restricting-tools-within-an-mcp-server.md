### Restricting tools within an MCP server

For even greater security, especially when dealing with third-party MCP servers,
you can restrict which specific tools from a server are exposed to the model.
This is done using the `includeTools` and `excludeTools` properties within a
server's definition. This allows you to use a subset of tools from a server
without allowing potentially dangerous ones.

Following the principle of least privilege, it is highly recommended to use
`includeTools` to create an allowlist of only the necessary tools.

**Example:** Only allow the `code-search` and `get-ticket-details` tools from a
third-party MCP server, even if the server offers other tools like
`delete-ticket`.

```json
{
  "mcp": {
    "allowed": ["third-party-analyzer"]
  },
  "mcpServers": {
    "third-party-analyzer": {
      "command": "/usr/local/bin/start-3p-analyzer.sh",
      "includeTools": ["code-search", "get-ticket-details"]
    }
  }
}
```

#### More secure pattern: Define and add to allowlist in system settings

To create a secure, centrally-managed catalog of tools, the system administrator
**must** do both of the following in the system-level `settings.json` file:

1.  **Define the full configuration** for every approved server in the
    `mcpServers` object. This ensures that even if a user defines a server with
    the same name, the secure system-level definition will take precedence.
2.  **Add the names** of those servers to an allowlist using the `mcp.allowed`
    setting. This is a critical security step that prevents users from running
    any servers that are not on this list. If this setting is omitted, the CLI
    will merge and allow any server defined by the user.

**Example system `settings.json`:**

1. Add the _names_ of all approved servers to an allowlist. This will prevent
   users from adding their own servers.

2. Provide the canonical _definition_ for each server on the allowlist.

```json
{
  "mcp": {
    "allowed": ["corp-data-api", "source-code-analyzer"]
  },
  "mcpServers": {
    "corp-data-api": {
      "command": "/usr/local/bin/start-corp-api.sh",
      "timeout": 5000
    },
    "source-code-analyzer": {
      "command": "/usr/local/bin/start-analyzer.sh"
    }
  }
}
```

This pattern is more secure because it uses both definition and an allowlist.
Any server a user defines will either be overridden by the system definition (if
it has the same name) or blocked because its name is not in the `mcp.allowed`
list.