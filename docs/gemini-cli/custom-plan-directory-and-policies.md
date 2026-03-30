### Custom plan directory and policies

By default, planning artifacts are stored in a managed temporary directory
outside your project: `~/.gemini/tmp/<project>/<session-id>/plans/`.

You can configure a custom directory for plans in your `settings.json`. For
example, to store plans in a `.gemini/plans` directory within your project:

```json
{
  "general": {
    "plan": {
      "directory": ".gemini/plans"
    }
  }
}
```

To maintain the safety of Plan Mode, user-configured paths for the plans
directory are restricted to the project root. This ensures that custom planning
locations defined within a project's workspace cannot be used to escape and
overwrite sensitive files elsewhere. Any user-configured directory must reside
within the project boundary.

Using a custom directory requires updating your
[policy engine](/docs/reference/policy-engine) configurations to allow
`write_file` and `replace` in that specific location. For example, to allow
writing to the `.gemini/plans` directory within your project, create a policy
file at `~/.gemini/policies/plan-custom-directory.toml`:

```toml
[[rule]]
toolName = ["write_file", "replace"]
decision = "allow"
priority = 100
modes = ["plan"]