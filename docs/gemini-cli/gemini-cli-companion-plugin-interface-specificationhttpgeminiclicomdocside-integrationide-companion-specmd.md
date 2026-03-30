# [Gemini CLI companion plugin: Interface specification](http://geminicli.com/docs/ide-integration/ide-companion-spec.md)


> Last Updated: September 15, 2025

This document defines the contract for building a companion plugin to enable
Gemini CLI's IDE mode. For VS Code, these features (native diffing, context
awareness) are provided by the official extension
([marketplace](https://marketplace.visualstudio.com/items?itemName=Google.gemini-cli-vscode-ide-companion)).
This specification is for contributors who wish to bring similar functionality
to other editors like JetBrains IDEs, Sublime Text, etc.