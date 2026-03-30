# By omitting "plan", this rule will not be active in Plan Mode.
modes = ["default", "autoEdit"]
```

#### Example: Automatically approve read-only MCP tools

By default, read-only MCP tools require user confirmation in Plan Mode. You can
use `toolAnnotations` and the `mcpName` wildcard to customize this behavior for
your specific environment.

`~/.gemini/policies/mcp-read-only.toml`

```toml
[[rule]]
toolName = "*"
mcpName = "*"
toolAnnotations = { readOnlyHint = true }
decision = "allow"
priority = 100
modes = ["plan"]
```

For more information on how the policy engine works, see the
[policy engine](/docs/reference/policy-engine) docs.

#### Example: Allow git commands in Plan Mode

This rule lets you check the repository status and see changes while in Plan
Mode.

`~/.gemini/policies/git-research.toml`

```toml
[[rule]]
toolName = "run_shell_command"
commandPrefix = ["git status", "git diff"]
decision = "allow"
priority = 100
modes = ["plan"]
```

#### Example: Enable custom subagents in Plan Mode

Built-in research [subagents](/docs/core/subagents) like
[`codebase_investigator`](/docs/core/subagents#codebase-investigator) and
[`cli_help`](/docs/core/subagents#cli-help-agent) are enabled by default in Plan
Mode. You can enable additional
[custom subagents](/docs/core/subagents#creating-custom-subagents) by adding a
rule to your policy.

`~/.gemini/policies/research-subagents.toml`

```toml
[[rule]]
toolName = "my_custom_subagent"
decision = "allow"
priority = 100
modes = ["plan"]
```

Tell Gemini CLI it can use these tools in your prompt, for example: _"You can
check ongoing changes in git."_