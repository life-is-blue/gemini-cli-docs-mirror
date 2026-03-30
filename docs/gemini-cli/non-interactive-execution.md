## Non-interactive execution

When running Gemini CLI in non-interactive environments (such as headless
scripts or CI/CD pipelines), Plan Mode optimizes for automated workflows:

- **Automatic transitions:** The policy engine automatically approves the
  `enter_plan_mode` and `exit_plan_mode` tools without prompting for user
  confirmation.
- **Automated implementation:** When exiting Plan Mode to execute the plan,
  Gemini CLI automatically switches to
  [YOLO mode](/docs/reference/policy-engine#approval-modes) instead of the
  standard Default mode. This allows the CLI to execute the implementation steps
  automatically without hanging on interactive tool approvals.

**Example:**

```bash
gemini --approval-mode plan -p "Analyze telemetry and suggest improvements"
```

[`plan.toml`]:
  https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/policy/policies/plan.toml
[Conductor]: https://github.com/gemini-cli-extensions/conductor
[open an issue]: https://github.com/google-gemini/gemini-cli/issues