### Extension not loading

If your extension doesn't appear in `/extensions list`:

- **Check the manifest:** Ensure `gemini-extension.json` is in the root
  directory and contains valid JSON.
- **Verify the name:** The `name` field in the manifest must match the extension
  directory name exactly.
- **Restart the CLI:** Extensions are loaded at the start of a session. Restart
  Gemini CLI after making changes to the manifest or linking a new extension.