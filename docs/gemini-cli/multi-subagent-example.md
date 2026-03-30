### Multi-subagent example

The loader explicitly supports multiple remote subagents defined in a single
Markdown file.

```markdown
---
- kind: remote
  name: remote-1
  agent_card_url: https://example.com/1
- kind: remote
  name: remote-2
  agent_card_url: https://example.com/2
---
```

<!-- prettier-ignore -->
> [!NOTE] Mixed local and remote agents, or multiple local agents, are not
> supported in a single file; the list format is currently remote-only.