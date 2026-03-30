## Using model steering

When model steering is enabled, Gemini CLI treats any text you type while the
agent is working as a steering hint.

1.  Start a task (for example, "Refactor the database service").
2.  While the agent is working (the spinner is visible), type your feedback in
    the input box.
3.  Press **Enter**.

Gemini CLI acknowledges your hint with a brief message and injects it directly
into the model's context for the very next turn. The model then re-evaluates its
current plan and adjusts its actions accordingly.