## Variables

Gemini CLI supports variable substitution in `gemini-extension.json` and
`hooks/hooks.json`.

| Variable           | Description                                     |
| :----------------- | :---------------------------------------------- |
| `${extensionPath}` | The absolute path to the extension's directory. |
| `${workspacePath}` | The absolute path to the current workspace.     |
| `${/}`             | The platform-specific path separator.           |