## 2. `exit_plan_mode` (ExitPlanMode)

`exit_plan_mode` signals that the planning phase is complete. It presents the
finalized plan to the user and requests approval to start the implementation.

- **Tool name:** `exit_plan_mode`
- **Display name:** Exit Plan Mode
- **File:** `exit-plan-mode.ts`
- **Parameters:**
  - `plan_path` (string, required): The path to the finalized Markdown plan
    file. This file MUST be located within the project's temporary plans
    directory (for example, `~/.gemini/tmp/<project>/plans/`).
- **Behavior:**
  - Validates that the `plan_path` is within the allowed directory and that the
    file exists and has content.
  - Presents the plan to the user for review.
  - If the user approves the plan:
    - Switches the CLI's approval mode to the user's chosen approval mode (
      `DEFAULT` or `AUTO_EDIT`).
    - Marks the plan as approved for implementation.
  - If the user rejects the plan:
    - Stays in Plan Mode.
    - Returns user feedback to the model to refine the plan.
- **Output (`llmContent`):**
  - On approval: A message indicating the plan was approved and the new approval
    mode.
  - On rejection: A message containing the user's feedback.
- **Confirmation:** Yes. Shows the finalized plan and asks for user approval to
  proceed with implementation.