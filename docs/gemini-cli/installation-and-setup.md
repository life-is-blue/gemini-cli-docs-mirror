### Installation and setup

There are three ways to set up the IDE integration:

#### 1. Automatic nudge (recommended)

When you run Gemini CLI inside a supported editor, it will automatically detect
your environment and prompt you to connect. Answering "Yes" will automatically
run the necessary setup, which includes installing the companion extension and
enabling the connection.

#### 2. Manual installation from CLI

If you previously dismissed the prompt or want to install the extension
manually, you can run the following command inside Gemini CLI:

```
/ide install
```

This will find the correct extension for your IDE and install it.

#### 3. Manual installation from a marketplace

You can also install the extension directly from a marketplace.

- **For Visual Studio Code:** Install from the
  [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=google.gemini-cli-vscode-ide-companion).
- **For VS Code forks:** To support forks of VS Code, the extension is also
  published on the
  [Open VSX Registry](https://open-vsx.org/extension/google/gemini-cli-vscode-ide-companion).
  Follow your editor's instructions for installing extensions from this
  registry.

<!-- prettier-ignore -->
> [!NOTE]
> The "Gemini CLI Companion" extension may appear towards the bottom of
> search results. If you don't see it immediately, try scrolling down or
> sorting by "Newly Published".
>
> After manually installing the extension, you must run `/ide enable` in the CLI
> to activate the integration.