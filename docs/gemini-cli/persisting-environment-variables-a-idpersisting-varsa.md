## Persisting environment variables <a id="persisting-vars"></a>

To avoid setting environment variables for every terminal session, you can
persist them with the following methods:

1.  **Add your environment variables to your shell configuration file:** Append
    the environment variable commands to your shell's startup file.

    **macOS/Linux** (for example, `~/.bashrc`, `~/.zshrc`, or `~/.profile`):

    ```bash
    echo 'export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"' >> ~/.bashrc
    source ~/.bashrc
    ```

    **Windows (PowerShell)** (for example, `$PROFILE`):

    ```powershell
    Add-Content -Path $PROFILE -Value '$env:GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"'
    . $PROFILE
    ```

<!-- prettier-ignore -->
> [!WARNING]
> Be aware that when you export API keys or service account
> paths in your shell configuration file, any process launched from that
> shell can read them.

2.  **Use a `.env` file:** Create a `.gemini/.env` file in your project
    directory or home directory. Gemini CLI automatically loads variables from
    the first `.env` file it finds, searching up from the current directory,
    then in your home directory's `.gemini/.env` (for example, `~/.gemini/.env`
    or `%USERPROFILE%\.gemini\.env`).

    Example for user-wide settings:

    **macOS/Linux**

    ```bash
    mkdir -p ~/.gemini
    cat >> ~/.gemini/.env <<'EOF'
    GOOGLE_CLOUD_PROJECT="your-project-id"
    # Add other variables like GEMINI_API_KEY as needed
    EOF
    ```

    **Windows (PowerShell)**

    ```powershell
    New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.gemini"
    @"
    GOOGLE_CLOUD_PROJECT="your-project-id"
    # Add other variables like GEMINI_API_KEY as needed
    "@ | Out-File -FilePath "$env:USERPROFILE\.gemini\.env" -Encoding utf8 -Append
    ```

Variables are loaded from the first file found, not merged.