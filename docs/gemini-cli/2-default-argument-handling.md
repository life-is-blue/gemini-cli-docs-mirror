### 2. Default argument handling

If your `prompt` does **not** contain the special placeholder `{{args}}`, the
CLI uses a default behavior for handling arguments.

If you provide arguments to the command (e.g., `/mycommand arg1`), the CLI will
append the full command you typed to the end of the prompt, separated by two
newlines. This allows the model to see both the original instructions and the
specific arguments you just provided.

If you do **not** provide any arguments (e.g., `/mycommand`), the prompt is sent
to the model exactly as it is, with nothing appended.

**Example (`changelog.toml`):**

This example shows how to create a robust command by defining a role for the
model, explaining where to find the user's input, and specifying the expected
format and behavior.

```toml