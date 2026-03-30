# Ask user for any tool call from any MCP server
[[rule]]
toolName = "*"
mcpName = "*"
decision = "ask_user"
priority = 10
```

**4. Targeting a tool name across all servers**

Use `mcpName = "*"` with a specific `toolName` to target that operation
regardless of which server provides it.

```toml