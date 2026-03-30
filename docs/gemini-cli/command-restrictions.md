## Command restrictions

<!-- prettier-ignore -->
> [!WARNING]
> The `tools.core` setting is an **allowlist for _all_ built-in
> tools**, not just shell commands. When you set `tools.core` to any value,
> _only_ the tools explicitly listed will be enabled. This includes all built-in
> tools like `read_file`, `write_file`, `glob`, `grep_search`, `list_directory`,
> `replace`, etc.

You can restrict the commands that can be executed by the `run_shell_command`
tool by using the `tools.core` and `tools.exclude` settings in your
configuration file.

- `tools.core`: To restrict `run_shell_command` to a specific set of commands,
  add entries to the `core` list under the `tools` category in the format
  `run_shell_command(<command>)`. For example,
  `"tools": {"core": ["run_shell_command(git)"]}` will only allow `git`
  commands. Including the generic `run_shell_command` acts as a wildcard,
  allowing any command not explicitly blocked.
- `tools.exclude` [DEPRECATED]: To block specific commands, use the
  [Policy Engine](/docs/reference/policy-engine). Historically, this setting
  allowed adding entries to the `exclude` list under the `tools` category in the
  format `run_shell_command(<command>)`. For example,
  `"tools": {"exclude": ["run_shell_command(rm)"]}` will block `rm` commands.

The validation logic is designed to be secure and flexible:

1.  **Command chaining disabled**: The tool automatically splits commands
    chained with `&&`, `||`, or `;` and validates each part separately. If any
    part of the chain is disallowed, the entire command is blocked.
2.  **Prefix matching**: The tool uses prefix matching. For example, if you
    allow `git`, you can run `git status` or `git log`.
3.  **Blocklist precedence**: The `tools.exclude` list is always checked first.
    If a command matches a blocked prefix, it will be denied, even if it also
    matches an allowed prefix in `tools.core`.