## 1. `enter_plan_mode` (EnterPlanMode)

`enter_plan_mode` switches the CLI to Plan Mode. This tool is typically called
by the agent when you ask it to "start a plan" using natural language. In this
mode, the agent is restricted to read-only tools to allow for safe exploration
and planning.

<!-- prettier-ignore -->
> [!NOTE]
> This tool is not available when the CLI is in YOLO mode.

- **Tool name:** `enter_plan_mode`
- **Display name:** Enter Plan Mode
- **File:** `enter-plan-mode.ts`
- **Parameters:**
  - `reason` (string, optional): A short reason explaining why the agent is
    entering plan mode (for example, "Starting a complex feature
    implementation").
- **Behavior:**
  - Switches the CLI's approval mode to `PLAN`.
  - Notifies the user that the agent has entered Plan Mode.
- **Output (`llmContent`):** A message indicating the switch, for example,
  `Switching to Plan mode.`
- **Confirmation:** Yes. The user is prompted to confirm entering Plan Mode.