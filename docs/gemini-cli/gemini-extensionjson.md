### `gemini-extension.json`

The manifest file defines the extension's behavior and configuration.

```json
{
  "name": "my-extension",
  "version": "1.0.0",
  "description": "My awesome extension",
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["${extensionPath}/my-server.js"],
      "cwd": "${extensionPath}"
    }
  },
  "contextFileName": "GEMINI.md",
  "excludeTools": ["run_shell_command"],
  "migratedTo": "https://github.com/new-owner/new-extension-repo",
  "plan": {
    "directory": ".gemini/plans"
  }
}
```

- `name`: The name of the extension. This is used to uniquely identify the
  extension and for conflict resolution when extension commands have the same
  name as user or project commands. The name should be lowercase or numbers and
  use dashes instead of underscores or spaces. This is how users will refer to
  your extension in the CLI. Note that we expect this name to match the
  extension directory name.
- `version`: The version of the extension.
- `description`: A short description of the extension. This will be displayed on
  [geminicli.com/extensions](https://geminicli.com/extensions).
- `migratedTo`: The URL of the new repository source for the extension. If this
  is set, the CLI will automatically check this new source for updates and
  migrate the extension's installation to the new source if an update is found.
- `mcpServers`: A map of MCP servers to settings. The key is the name of the
  server, and the value is the server configuration. These servers will be
  loaded on startup just like MCP servers defined in a
  [`settings.json` file](/docs/reference/configuration). If both an extension
  and a `settings.json` file define an MCP server with the same name, the server
  defined in the `settings.json` file takes precedence.
  - Note that all MCP server configuration options are supported except for
    `trust`.
  - For portability, you should use `${extensionPath}` to refer to files within
    your extension directory.
  - Separate your executable and its arguments using `command` and `args`
    instead of putting them both in `command`.
- `contextFileName`: The name of the file that contains the context for the
  extension. This will be used to load the context from the extension directory.
  If this property is not used but a `GEMINI.md` file is present in your
  extension directory, then that file will be loaded.
- `excludeTools`: An array of tool names to exclude from the model. You can also
  specify command-specific restrictions for tools that support it, like the
  `run_shell_command` tool. For example,
  `"excludeTools": ["run_shell_command(rm -rf)"]` will block the `rm -rf`
  command. Note that this differs from the MCP server `excludeTools`
  functionality, which can be listed in the MCP server config.
- `plan`: Planning features configuration.
  - `directory`: The directory where planning artifacts are stored. This serves
    as a fallback if the user hasn't specified a plan directory in their
    settings. If not specified by either the extension or the user, the default
    is `~/.gemini/tmp/<project>/<session-id>/plans/`.

When Gemini CLI starts, it loads all the extensions and merges their
configurations. If there are any conflicts, the workspace configuration takes
precedence.