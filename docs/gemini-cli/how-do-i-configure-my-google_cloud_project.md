### How do I configure my `GOOGLE_CLOUD_PROJECT`?

You can configure your Google Cloud Project ID using an environment variable.

Set the `GOOGLE_CLOUD_PROJECT` environment variable in your shell:

**macOS/Linux**

```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
```

**Windows (PowerShell)**

```powershell
$env:GOOGLE_CLOUD_PROJECT="your-project-id"
```

To make this setting permanent, add this line to your shell's startup file
(e.g., `~/.bashrc`, `~/.zshrc`).