# Allows the `search` tool on the `my-jira-server` MCP
[[rule]]
mcpName = "my-jira-server"
toolName = "search"
decision = "allow"
priority = 200
```

**2. Targeting all tools on a specific server**

Specify only the `mcpName` to apply a rule to every tool provided by that
server.

**Note:** This applies to all decision types (`allow`, `deny`, `ask_user`).

```toml