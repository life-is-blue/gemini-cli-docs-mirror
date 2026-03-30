### Make scripts executable

Always make hook scripts executable on macOS/Linux:

```bash
chmod +x .gemini/hooks/*.sh
chmod +x .gemini/hooks/*.js

```

**Windows Note**: On Windows, PowerShell scripts (`.ps1`) don't use `chmod`, but
you may need to ensure your execution policy allows them to run (e.g.,
`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`).