## Step 4: Link your extension

Link your extension to your Gemini CLI installation for local development.

1.  **Install dependencies:**

    ```bash
    cd my-first-extension
    npm install
    ```

2.  **Link the extension:**

    The `link` command creates a symbolic link from the Gemini CLI extensions
    directory to your development directory. Changes you make are reflected
    immediately.

    ```bash
    gemini extensions link .
    ```

Restart your Gemini CLI session to use the new `fetch_posts` tool. Test it by
asking: "fetch posts".