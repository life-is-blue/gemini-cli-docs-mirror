### Custom commands

Provide [custom commands](/docs/cli/custom-commands) by placing TOML files in a
`commands/` subdirectory. Gemini CLI uses the directory structure to determine
the command name.

For an extension named `gcp`:

- `commands/deploy.toml` becomes `/deploy`
- `commands/gcs/sync.toml` becomes `/gcs:sync` (namespaced with a colon)