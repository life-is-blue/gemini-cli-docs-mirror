### Enabling interactive commands

To enable interactive commands, you need to set the
`tools.shell.enableInteractiveShell` setting to `true`. This will use `node-pty`
for shell command execution, which allows for interactive sessions. If
`node-pty` is not available, it will fall back to the `child_process`
implementation, which does not support interactive commands.

**Example `settings.json`:**

```json
{
  "tools": {
    "shell": {
      "enableInteractiveShell": true
    }
  }
}
```