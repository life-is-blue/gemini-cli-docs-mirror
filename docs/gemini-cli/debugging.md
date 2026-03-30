### Debugging

#### VS Code

0.  Run the CLI to interactively debug in VS Code with `F5`
1.  Start the CLI in debug mode from the root directory:
    ```bash
    npm run debug
    ```
    This command runs `node --inspect-brk dist/gemini.js` within the
    `packages/cli` directory, pausing execution until a debugger attaches. You
    can then open `chrome://inspect` in your Chrome browser to connect to the
    debugger.
2.  In VS Code, use the "Attach" launch configuration (found in
    `.vscode/launch.json`).

Alternatively, you can use the "Launch Program" configuration in VS Code if you
prefer to launch the currently open file directly, but 'F5' is generally
recommended.

To hit a breakpoint inside the sandbox container run:

```bash
DEBUG=1 gemini
```

**Note:** If you have `DEBUG=true` in a project's `.env` file, it won't affect
gemini-cli due to automatic exclusion. Use `.gemini/.env` files for gemini-cli
specific debug settings.