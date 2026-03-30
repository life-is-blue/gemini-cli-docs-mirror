## Quick start

To create your first policy:

1.  **Create the policy directory** if it doesn't exist:

    **macOS/Linux**

    ```bash
    mkdir -p ~/.gemini/policies
    ```

    **Windows (PowerShell)**

    ```powershell
    New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.gemini\policies"
    ```

2.  **Create a new policy file** (e.g., `~/.gemini/policies/my-rules.toml`). You
    can use any filename ending in `.toml`; all such files in this directory
    will be loaded and combined:
    ```toml
    [[rule]]
    toolName = "run_shell_command"
    commandPrefix = "git status"
    decision = "allow"
    priority = 100
    ```
3.  **Run a command** that triggers the policy (e.g., ask Gemini CLI to
    `git status`). The tool will now execute automatically without prompting for
    confirmation.