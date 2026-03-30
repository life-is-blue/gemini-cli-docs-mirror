## How to run commands directly (`!`)

Sometimes you just need to check a file size or git status without asking the AI
to do it for you. You can pass commands directly to your shell using the `!`
prefix.

**Example:** `!ls -la`

This executes `ls -la` immediately and prints the output to your terminal.
Gemini CLI also records the command and its output in the current session
context, so the model can reference it in follow-up prompts. Very large outputs
may be truncated.