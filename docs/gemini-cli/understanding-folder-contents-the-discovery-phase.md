## Understanding folder contents: The discovery phase

Before you make a choice, the Gemini CLI performs a **discovery phase** to scan
the folder for potential configurations. This information is displayed in the
trust dialog to help you make an informed decision.

The discovery UI lists the following categories of items found in the project:

- **Commands**: Custom `.toml` command definitions that add new functionality.
- **MCP Servers**: Configured Model Context Protocol servers that the CLI will
  attempt to connect to.
- **Hooks**: System or custom hooks that can intercept and modify CLI behavior.
- **Skills**: Local agent skills that provide specialized capabilities.
- **Setting overrides**: Any project-specific configurations that override your
  global user settings.