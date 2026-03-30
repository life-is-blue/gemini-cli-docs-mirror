## How to prepare your credentials

Most MCP servers require authentication. For GitHub, you need a PAT.

1.  Create a [fine-grained PAT](https://github.com/settings/tokens?type=beta).
2.  Grant it **Read** access to **Metadata** and **Contents**, and
    **Read/Write** access to **Issues** and **Pull Requests**.
3.  Store it in your environment:

**macOS/Linux**

```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="github_pat_..."
```

**Windows (PowerShell)**

```powershell
$env:GITHUB_PERSONAL_ACCESS_TOKEN="github_pat_..."
```