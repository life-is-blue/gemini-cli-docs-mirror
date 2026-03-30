# Pass all arguments to the real Gemini CLI executable.
exec "$REAL_GEMINI_PATH" "$@"
```

By deploying this script, the `GEMINI_CLI_SYSTEM_SETTINGS_PATH` is set within
the script's environment, and the `exec` command replaces the script process
with the actual Gemini CLI process, which inherits the environment variable.
This makes it significantly more difficult for a user to bypass the enforced
settings.

**PowerShell Profile (Windows alternative):**

On Windows, administrators can achieve similar results by adding the environment
variable to the system-wide or user-specific PowerShell profile:

```powershell
Add-Content -Path $PROFILE -Value '$env:GEMINI_CLI_SYSTEM_SETTINGS_PATH="C:\ProgramData\gemini-cli\settings.json"'
```