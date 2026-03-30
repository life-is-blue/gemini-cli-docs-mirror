### Isolation and recursion protection

Each subagent runs in its own isolated context loop. This means:

- **Independent history:** The subagent's conversation history does not bloat
  the main agent's context.
- **Isolated tools:** The subagent only has access to the tools you explicitly
  grant it.
- **Recursion protection:** To prevent infinite loops and excessive token usage,
  subagents **cannot** call other subagents. If a subagent is granted the `*`
  tool wildcard, it will still be unable to see or invoke other agents.