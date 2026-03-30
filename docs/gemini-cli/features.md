### Features

- **Workspace context:** The CLI automatically gains awareness of your workspace
  to provide more relevant and accurate responses. This context includes:
  - The **10 most recently accessed files** in your workspace.
  - Your active cursor position.
  - Any text you have selected (up to a 16KB limit; longer selections will be
    truncated).

- **Native diffing:** When Gemini suggests code modifications, you can view the
  changes directly within your IDE's native diff viewer. This lets you review,
  edit, and accept or reject the suggested changes seamlessly.

- **VS Code commands:** You can access Gemini CLI features directly from the VS
  Code Command Palette (`Cmd+Shift+P` or `Ctrl+Shift+P`):
  - `Gemini CLI: Run`: Starts a new Gemini CLI session in the integrated
    terminal.
  - `Gemini CLI: Accept Diff`: Accepts the changes in the active diff editor.
  - `Gemini CLI: Close Diff Editor`: Rejects the changes and closes the active
    diff editor.
  - `Gemini CLI: View Third-Party Notices`: Displays the third-party notices for
    the extension.