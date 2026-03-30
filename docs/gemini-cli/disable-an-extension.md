### Disable an extension

Extensions are enabled globally by default. You can disable an extension
entirely or for a specific workspace.

```bash
gemini extensions disable <name> [--scope <scope>]
```

- `<name>`: The name of the extension to disable.
- `--scope`: The scope to disable the extension in (`user` or `workspace`).