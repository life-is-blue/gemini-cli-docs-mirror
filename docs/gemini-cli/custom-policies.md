### Custom policies

Plan Mode's default tool restrictions are managed by the
[policy engine](/docs/reference/policy-engine) and defined in the built-in
[`plan.toml`] file. The built-in policy (Tier 1) enforces the read-only state,
but you can customize these rules by creating your own policies in your
`~/.gemini/policies/` directory (Tier 2).

#### Global vs. mode-specific rules

As described in the
[policy engine documentation](/docs/reference/policy-engine#approval-modes), any
rule that does not explicitly specify `modes` is considered "always active" and
will apply to Plan Mode as well.

If you want a rule to apply to other modes but _not_ to Plan Mode, you must
explicitly specify the target modes. For example, to allow `npm test` in default
and Auto-Edit modes but not in Plan Mode:

```toml
[[rule]]
toolName = "run_shell_command"
commandPrefix = "npm test"
decision = "allow"
priority = 100