### Removing a server (`gemini mcp remove`)

To delete a server from your configuration, use the `remove` command with the
server's name.

**Command:**

```bash
gemini mcp remove <name>
```

**Options (flags):**

- `-s, --scope`: Configuration scope (user or project). [default: "project"]

**Example:**

```bash
gemini mcp remove my-server
```

This will find and delete the "my-server" entry from the `mcpServers` object in
the appropriate `settings.json` file based on the scope (`-s, --scope`).