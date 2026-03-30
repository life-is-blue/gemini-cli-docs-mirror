## How it works

When you submit a steering hint, Gemini CLI performs the following actions:

1.  **Immediate acknowledgment:** It uses a small, fast model to generate a
    one-sentence acknowledgment so you know your hint was received.
2.  **Context injection:** It prepends an internal instruction to your hint that
    tells the main agent to:
    - Re-evaluate the active plan.
    - Classify the update (for example, as a new task or extra context).
    - Apply minimal-diff changes to affected tasks.
3.  **Real-time update:** The hint is delivered to the agent at the beginning of
    its next turn, ensuring the most immediate course correction possible.