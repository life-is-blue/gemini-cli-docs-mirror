### Command restriction examples

**Allow only specific command prefixes**

To allow only `git` and `npm` commands, and block all others:

```json
{
  "tools": {
    "core": ["run_shell_command(git)", "run_shell_command(npm)"]
  }
}
```

- `git status`: Allowed
- `npm install`: Allowed
- `ls -l`: Blocked

**Block specific command prefixes**

To block `rm` and allow all other commands:

```json
{
  "tools": {
    "core": ["run_shell_command"],
    "exclude": ["run_shell_command(rm)"]
  }
}
```

- `rm -rf /`: Blocked
- `git status`: Allowed
- `npm install`: Allowed

**Blocklist takes precedence**

If a command prefix is in both `tools.core` and `tools.exclude`, it will be
blocked.

- **`tools.shell.enableInteractiveShell`**: (boolean) Uses `node-pty` for
  real-time interaction.
- **`tools.shell.showColor`**: (boolean) Preserves ANSI colors in output.
- **`tools.shell.inactivityTimeout`**: (number) Seconds to wait for output
  before killing the process.