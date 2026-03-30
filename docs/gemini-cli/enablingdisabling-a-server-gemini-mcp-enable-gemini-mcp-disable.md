### Enabling/disabling a server (`gemini mcp enable`, `gemini mcp disable`)

Temporarily disable an MCP server without removing its configuration, or
re-enable a previously disabled server.

**Commands:**

```bash
gemini mcp enable <name> [--session]
gemini mcp disable <name> [--session]
```

**Options (flags):**

- `--session`: Apply change only for this session (not persisted to file).

Disabled servers appear in `/mcp` status as "Disabled" but won't connect or
provide tools. Enablement state is stored in
`~/.gemini/mcp-server-enablement.json`.

The same commands are available as slash commands during an active session:
`/mcp enable <name>` and `/mcp disable <name>`.