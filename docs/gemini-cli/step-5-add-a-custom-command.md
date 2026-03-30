## Step 5: Add a custom command

Custom commands create shortcuts for complex prompts.

1.  Create a `commands` directory and a subdirectory for your command group:

    **macOS/Linux**

    ```bash
    mkdir -p commands/fs
    ```

    **Windows (PowerShell)**

    ```powershell
    New-Item -ItemType Directory -Force -Path "commands\fs"
    ```

2.  Create a file named `commands/fs/grep-code.toml`:

    ```toml
    prompt = """
    Please summarize the findings for the pattern `{{args}}`.

    Search Results:
    !{grep -r {{args}} .}
    """
    ```

    This command, `/fs:grep-code`, takes an argument, runs the `grep` shell
    command, and pipes the results into a prompt for summarization.

After saving the file, restart Gemini CLI. Run `/fs:grep-code "some pattern"` to
use your new command.