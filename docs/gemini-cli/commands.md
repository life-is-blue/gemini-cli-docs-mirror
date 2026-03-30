### `/commands`

- **Description:** Manage custom slash commands loaded from `.toml` files.
- **Sub-commands:**
  - **`reload`**:
    - **Description:** Reload custom command definitions from all sources
      (user-level `~/.gemini/commands/`, project-level
      `<project>/.gemini/commands/`, MCP prompts, and extensions). Use this to
      pick up new or modified `.toml` files without restarting the CLI.
    - **Usage:** `/commands reload`