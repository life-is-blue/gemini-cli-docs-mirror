# Denies all tools from the `untrusted-server` MCP
[[rule]]
mcpName = "untrusted-server"
decision = "deny"
priority = 500
denyMessage = "This server is not trusted by the admin."
```

**3. Targeting all MCP servers**

Use `mcpName = "*"` to create a rule that applies to **all** tools from **any**
registered MCP server. This is useful for setting category-wide defaults.

```toml