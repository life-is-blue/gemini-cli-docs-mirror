### Less secure pattern: Omitting the allowlist

If the administrator defines the `mcpServers` object but fails to also specify
the `mcp.allowed` allowlist, users may add their own servers.

**Example system `settings.json`:**

This configuration defines servers but does not enforce the allowlist. The
administrator has NOT included the "mcp.allowed" setting.

```json
{
  "mcpServers": {
    "corp-data-api": {
      "command": "/usr/local/bin/start-corp-api.sh"
    }
  }
}
```

In this scenario, a user can add their own server in their local
`settings.json`. Because there is no `mcp.allowed` list to filter the merged
results, the user's server will be added to the list of available tools and
allowed to run.