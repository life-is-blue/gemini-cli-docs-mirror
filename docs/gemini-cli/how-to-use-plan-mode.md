## How to use Plan Mode

Plan Mode lets you collaborate with Gemini CLI to design a solution before
Gemini CLI takes action.

1.  **Provide a goal:** Start by describing what you want to achieve. Gemini CLI
    will then enter Plan Mode (if it's not already) to research the task.
2.  **Review research and provide input:** As Gemini CLI analyzes your codebase,
    it may ask you questions or present different implementation options using
    [`ask_user`](/docs/tools/ask-user). Provide your preferences to help guide
    the design.
3.  **Review the plan:** Once Gemini CLI has a proposed strategy, it creates a
    detailed implementation plan as a Markdown file in your plans directory.
    - **View:** You can open and read this file to understand the proposed
      changes.
    - **Edit:** Press `Ctrl+X` to open the plan directly in your configured
      external editor.

4.  **Approve or iterate:** Gemini CLI will present the finalized plan for your
    approval.
    - **Approve:** If you're satisfied with the plan, approve it to start the
      implementation immediately: **Yes, automatically accept edits** or **Yes,
      manually accept edits**.
    - **Iterate:** If the plan needs adjustments, provide feedback in the input
      box or [edit the plan file directly](#collaborative-plan-editing). Gemini
      CLI will refine the strategy and update the plan.
    - **Cancel:** You can cancel your plan with `Esc`.

For more complex or specialized planning tasks, you can
[customize the planning workflow with skills](#custom-planning-with-skills).