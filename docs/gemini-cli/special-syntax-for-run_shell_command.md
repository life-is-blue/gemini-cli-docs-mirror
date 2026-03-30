### Special syntax for `run_shell_command`

To simplify writing policies for `run_shell_command`, you can use
`commandPrefix` or `commandRegex` instead of the more complex `argsPattern`.

- `commandPrefix`: Matches if the `command` argument starts with the given
  string.
- `commandRegex`: Matches if the `command` argument matches the given regular
  expression.

**Example:**

This rule will ask for user confirmation before executing any `git` command.

```toml
[[rule]]
toolName = "run_shell_command"
commandPrefix = "git"
decision = "ask_user"
priority = 100
```