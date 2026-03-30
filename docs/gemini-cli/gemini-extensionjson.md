### `gemini-extension.json`

The manifest file tells Gemini CLI how to load and use your extension.

```json
{
  "name": "mcp-server-example",
  "version": "1.0.0",
  "mcpServers": {
    "nodeServer": {
      "command": "node",
      "args": ["${extensionPath}${/}example.js"],
      "cwd": "${extensionPath}"
    }
  }
}
```

- `name`: The unique name for your extension.
- `version`: The version of your extension.
- `mcpServers`: Defines Model Context Protocol (MCP) servers to add new tools.
  - `command`, `args`, `cwd`: Specify how to start your server. The
    `${extensionPath}` variable is replaced with the absolute path to your
    extension's directory.