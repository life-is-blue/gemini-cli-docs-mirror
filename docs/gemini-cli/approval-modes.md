### Approval modes

Approval modes allow the policy engine to apply different sets of rules based on
the CLI's operational mode. A rule can be associated with one or more modes
(e.g., `yolo`, `autoEdit`, `plan`). The rule will only be active if the CLI is
running in one of its specified modes. If a rule has no modes specified, it is
always active.

- `default`: The standard interactive mode where most write tools require
  confirmation.
- `autoEdit`: Optimized for automated code editing; some write tools may be
  auto-approved.
- `plan`: A strict, read-only mode for research and design. See
  [Customizing Plan Mode Policies](/docs/cli/plan-mode#customizing-policies).
- `yolo`: A mode where all tools are auto-approved (use with extreme caution).