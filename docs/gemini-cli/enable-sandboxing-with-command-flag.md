# Enable sandboxing with command flag
gemini -s -p "analyze the code structure"
```

**Use environment variable**

**macOS/Linux**

```bash
export GEMINI_SANDBOX=true
gemini -p "run the test suite"
```

**Windows (PowerShell)**

```powershell
$env:GEMINI_SANDBOX="true"
gemini -p "run the test suite"
```

**Configure in settings.json**

```json
{
  "tools": {
    "sandbox": "docker"
  }
}
```