## Core concepts

The policy engine operates on a set of rules. Each rule is a combination of
conditions and a resulting decision. When a large language model wants to
execute a tool, the policy engine evaluates all rules to find the
highest-priority rule that matches the tool call.

A rule consists of the following main components:

- **Conditions**: Criteria that a tool call must meet for the rule to apply.
  This can include the tool's name, the arguments provided to it, or the current
  approval mode.
- **Decision**: The action to take if the rule matches (`allow`, `deny`, or
  `ask_user`).
- **Priority**: A number that determines the rule's precedence. Higher numbers
  win.

For example, this rule will ask for user confirmation before executing any `git`
command.

```toml
[[rule]]
toolName = "run_shell_command"
commandPrefix = "git"
decision = "ask_user"
priority = 100
```