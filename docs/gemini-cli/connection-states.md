### Connection states

The MCP integration tracks several states:

#### Overriding extension configurations

If an MCP server is provided by an extension (for example, the
`google-workspace` extension), you can still override its settings in your local
`settings.json`. Gemini CLI merges your local configuration with the extension's
defaults:

- **Tool lists:** Tool lists are merged securely to ensure the most restrictive
  policy wins:
  - **Exclusions (`excludeTools`):** Arrays are combined (unioned). If either
    source blocks a tool, it remains disabled.
  - **Inclusions (`includeTools`):** Arrays are intersected. If both sources
    provide an allowlist, only tools present in **both** lists are enabled. If
    only one source provides an allowlist, that list is respected.
  - **Precedence:** `excludeTools` always takes precedence over `includeTools`.

  This ensures you always have veto power over tools provided by an extension
  and that an extension cannot re-enable tools you have omitted from your
  personal allowlist.

- **Environment variables:** The `env` objects are merged. If the same variable
  is defined in both places, your local value takes precedence.
- **Scalar properties:** Properties like `command`, `url`, and `timeout` are
  replaced by your local values if provided.

**Example override:**

```json
{
  "mcpServers": {
    "google-workspace": {
      "excludeTools": ["gmail.send"]
    }
  }
}
```

#### Server status (`MCPServerStatus`)

- **`DISCONNECTED`:** Server is not connected or has errors
- **`CONNECTING`:** Connection attempt in progress
- **`CONNECTED`:** Server is connected and ready

#### Discovery state (`MCPDiscoveryState`)

- **`NOT_STARTED`:** Discovery hasn't begun
- **`IN_PROGRESS`:** Currently discovering servers
- **`COMPLETED`:** Discovery finished (with or without errors)