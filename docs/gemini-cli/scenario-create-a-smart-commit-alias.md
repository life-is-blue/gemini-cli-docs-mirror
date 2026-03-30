### Scenario: Create a "Smart Commit" alias

You can add a function to your shell configuration to create a `git commit`
wrapper that writes the message for you.

**macOS/Linux (Bash/Zsh)**

1.  Open your `.zshrc` file (or `.bashrc` if you use Bash) in your preferred
    text editor.

    ```bash
    nano ~/.zshrc
    ```

    **Note**: If you use VS Code, you can run `code ~/.zshrc`.

2.  Scroll to the very bottom of the file and paste this code:

    ```bash
    function gcommit() {
      # Get the diff of staged changes
      diff=$(git diff --staged)

      if [ -z "$diff" ]; then
        echo "No staged changes to commit."
        return 1
      fi

      # Ask Gemini to write the message
      echo "Generating commit message..."
      msg=$(echo "$diff" | gemini -p "Write a concise Conventional Commit message for this diff. Output ONLY the message.")

      # Commit with the generated message
      git commit -m "$msg"
    }
    ```

    Save your file and exit.

3.  Run this command to make the function available immediately:

    ```bash
    source ~/.zshrc
    ```

**Windows (PowerShell)**

1.  Open your PowerShell profile in your preferred text editor.

    ```powershell
    notepad $PROFILE
    ```

2.  Scroll to the very bottom of the file and paste this code:

    ```powershell
    function gcommit {
      # Get the diff of staged changes
      $diff = git diff --staged

      if (-not $diff) {
        Write-Host "No staged changes to commit."
        return
      }

      # Ask Gemini to write the message
      Write-Host "Generating commit message..."
      $msg = $diff | gemini -p "Write a concise Conventional Commit message for this diff. Output ONLY the message."

      # Commit with the generated message
      git commit -m "$msg"
    }
    ```

    Save your file and exit.

3.  Run this command to make the function available immediately:

    ```powershell
    . $PROFILE
    ```

4.  Use your new command:

    ```bash
    gcommit
    ```

    Gemini CLI will analyze your staged changes and commit them with a generated
    message.