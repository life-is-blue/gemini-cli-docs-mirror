# [IDE Integration](http://geminicli.com/docs/ide-integration.md)


Gemini CLI can integrate with your IDE to provide a more seamless and
context-aware experience. This integration allows the CLI to understand your
workspace better and enables powerful features like native in-editor diffing.

There are two primary ways to integrate Gemini CLI with an IDE:

1.  **VS Code companion extension**: Install the "Gemini CLI Companion"
    extension on [Antigravity](https://antigravity.google),
    [Visual Studio Code](https://code.visualstudio.com/), or other VS Code
    compatible editors.
2.  **Agent Client Protocol (ACP)**: An open protocol for interoperability
    between AI coding agents and IDEs. This method is used for integrations with
    tools like JetBrains and Zed, which leverage the ACP Agent Registry for easy
    discovery and installation of compatible agents like Gemini CLI.