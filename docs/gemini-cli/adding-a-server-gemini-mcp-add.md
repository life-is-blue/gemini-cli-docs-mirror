### Adding a server (`gemini mcp add`)

The `add` command configures a new MCP server in your `settings.json`. Based on
the scope (`-s, --scope`), it will be added to either the user config
`~/.gemini/settings.json` or the project config `.gemini/settings.json` file.

**Command:**

```bash
gemini mcp add [options] <name> <commandOrUrl> [args...]
```

- `<name>`: A unique name for the server.
- `<commandOrUrl>`: The command to execute (for `stdio`) or the URL (for
  `http`/`sse`).
- `[args...]`: Optional arguments for a `stdio` command.

**Options (flags):**

- `-s, --scope`: Configuration scope (user or project). [default: "project"]
- `-t, --transport`: Transport type (stdio, sse, http). [default: "stdio"]
- `-e, --env`: Set environment variables (e.g. -e KEY=value).
- `-H, --header`: Set HTTP headers for SSE and HTTP transports (e.g. -H
  "X-Api-Key: abc123" -H "Authorization: Bearer abc123").
- `--timeout`: Set connection timeout in milliseconds.
- `--trust`: Trust the server (bypass all tool call confirmation prompts).
- `--description`: Set the description for the server.
- `--include-tools`: A comma-separated list of tools to include.
- `--exclude-tools`: A comma-separated list of tools to exclude.

#### Adding an stdio server

This is the default transport for running local servers.

```bash