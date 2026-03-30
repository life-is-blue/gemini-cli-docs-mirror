### 3. Executing shell commands with `!{...}`

You can make your commands dynamic by executing shell commands directly within
your `prompt` and injecting their output. This is ideal for gathering context
from your local environment, like reading file content or checking the status of
Git.

When a custom command attempts to execute a shell command, Gemini CLI will now
prompt you for confirmation before proceeding. This is a security measure to
ensure that only intended commands can be run.

**How it works:**

1.  **Inject commands:** Use the `!{...}` syntax.
2.  **Argument substitution:** If `{{args}}` is present inside the block, it is
    automatically shell-escaped (see
    [Context-Aware Injection](#1-context-aware-injection-with-args) above).
3.  **Robust parsing:** The parser correctly handles complex shell commands that
    include nested braces, such as JSON payloads. The content inside `!{...}`
    must have balanced braces (`{` and `}`). If you need to execute a command
    containing unbalanced braces, consider wrapping it in an external script
    file and calling the script within the `!{...}` block.
4.  **Security check and confirmation:** The CLI performs a security check on
    the final, resolved command (after arguments are escaped and substituted). A
    dialog will appear showing the exact command(s) to be executed.
5.  **Execution and error reporting:** The command is executed. If the command
    fails, the output injected into the prompt will include the error messages
    (stderr) followed by a status line, e.g.,
    `[Shell command exited with code 1]`. This helps the model understand the
    context of the failure.

**Example (`git/commit.toml`):**

This command gets the staged git diff and uses it to ask the model to write a
commit message.

````toml