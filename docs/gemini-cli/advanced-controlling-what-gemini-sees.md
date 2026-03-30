## Advanced: Controlling what Gemini sees

By default, Gemini CLI respects your `.gitignore` file. It won't read or search
through `node_modules`, build artifacts, or other ignored paths.

If you have sensitive files (like `.env`) or large assets that you want to keep
hidden from the AI _without_ ignoring them in Git, you can create a
`.geminiignore` file in your project root.

**Example `.geminiignore`:**

```text
.env
local-db-dump.sql
private-notes.md
```