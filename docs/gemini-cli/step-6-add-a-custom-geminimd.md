## Step 6: Add a custom `GEMINI.md`

Provide persistent context to the model by adding a `GEMINI.md` file to your
extension. This is useful for setting behavior or providing essential tool
information.

1.  Create a file named `GEMINI.md` in the root of your extension directory:

    ```markdown
    # My First Extension Instructions

    You are an expert developer assistant. When the user asks you to fetch
    posts, use the `fetch_posts` tool. Be concise in your responses.
    ```

2.  Update your `gemini-extension.json` to load this file:

    ```json
    {
      "name": "my-first-extension",
      "version": "1.0.0",
      "contextFileName": "GEMINI.md",
      "mcpServers": {
        "nodeServer": {
          "command": "node",
          "args": ["${extensionPath}${/}example.js"],
          "cwd": "${extensionPath}"
        }
      }
    }
    ```

Restart Gemini CLI. The model now has the context from your `GEMINI.md` file in
every session where the extension is active.