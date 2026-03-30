### Custom identification

You can provide a custom identifier for your own scripts or automation by
setting the `GEMINI_CLI_SURFACE` environment variable. This is useful for
tracking specific internal tools or distribution channels in your GCP logs.

**macOS/Linux**

```bash
export GEMINI_CLI_SURFACE="my-custom-tool"
```

**Windows (PowerShell)**

```powershell
$env:GEMINI_CLI_SURFACE="my-custom-tool"
```

When set, the value appears at the end of the `User-Agent` parenthetical:
`GeminiCLI/0.34.0/gemini-pro (linux; x64; my-custom-tool)`