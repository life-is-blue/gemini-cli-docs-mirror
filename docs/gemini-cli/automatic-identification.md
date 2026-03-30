### Automatic identification

Most integrated environments are identified automatically without additional
configuration. The identifier is included as a prefix to the `User-Agent` and as
a "surface" tag in the parenthetical metadata.

| Environment                         | User-Agent Prefix            | Surface Tag |
| :---------------------------------- | :--------------------------- | :---------- |
| **Gemini Code Assist (Agent Mode)** | `GeminiCLI-a2a-server`       | `vscode`    |
| **Zed (via ACP)**                   | `GeminiCLI-acp-zed`          | `zed`       |
| **XCode (via ACP)**                 | `GeminiCLI-acp-xcode`        | `xcode`     |
| **IntelliJ IDEA (via ACP)**         | `GeminiCLI-acp-intellijidea` | `jetbrains` |
| **Standard Terminal**               | `GeminiCLI`                  | `terminal`  |

**Example User-Agent:**
`GeminiCLI-a2a-server/0.34.0/gemini-pro (linux; x64; vscode)`