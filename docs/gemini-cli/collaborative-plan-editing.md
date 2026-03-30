### Collaborative plan editing

You can collaborate with Gemini CLI by making direct changes or leaving comments
in the implementation plan. This is often faster and more precise than
describing complex changes in natural language.

1.  **Open the plan:** Press `Ctrl+X` when Gemini CLI presents a plan for
    review.
2.  **Edit or comment:** The plan opens in your configured external editor (for
    example, VS Code or Vim). You can:
    - **Modify steps:** Directly reorder, delete, or rewrite implementation
      steps.
    - **Leave comments:** Add inline questions or feedback (for example, "Wait,
      shouldn't we use the existing `Logger` class here?").
3.  **Save and close:** Save your changes and close the editor.
4.  **Review and refine:** Gemini CLI automatically detects the changes, reviews
    your comments, and adjusts the implementation strategy. It then presents the
    refined plan for your final approval.