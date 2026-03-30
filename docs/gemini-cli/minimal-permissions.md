### Minimal permissions

Only request the permissions your MCP server needs to function. Avoid giving the
model broad access (such as full shell access) if restricted tools are
sufficient.

If your extension uses powerful tools like `run_shell_command`, restrict them in
your `gemini-extension.json` file:

```json
{
  "name": "my-safe-extension",
  "excludeTools": ["run_shell_command(rm -rf *)"]
}
```

This ensures the CLI blocks dangerous commands even if the model attempts to
execute them.