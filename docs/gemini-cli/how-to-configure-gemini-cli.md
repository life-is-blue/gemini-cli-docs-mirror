## How to configure Gemini CLI

You tell Gemini about new servers by editing your `settings.json`.

1.  Open `~/.gemini/settings.json` (or the project-specific
    `.gemini/settings.json`).
2.  Add the `mcpServers` block. This tells Gemini: "Run this docker container
    and talk to it."

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server:latest"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

<!-- prettier-ignore -->
> [!NOTE]
> The `command` is `docker`, and the rest are arguments passed to it. We
> map the local environment variable into the container so your secret isn't
> hardcoded in the config file.