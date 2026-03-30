## Naming and namespacing

The name of a command is determined by its file path relative to its `commands`
directory. Subdirectories are used to create namespaced commands, with the path
separator (`/` or `\`) being converted to a colon (`:`).

- A file at `~/.gemini/commands/test.toml` becomes the command `/test`.
- A file at `<project>/.gemini/commands/git/commit.toml` becomes the namespaced
  command `/git:commit`.

<!-- prettier-ignore -->
> [!TIP]
> After creating or modifying `.toml` command files, run
> `/commands reload` to pick up your changes without restarting the CLI.