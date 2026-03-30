## Under the hood

For developers, the tool system is designed to be extensible and robust. The
`ToolRegistry` class manages all available tools.

You can extend Gemini CLI with custom tools by configuring
`tools.discoveryCommand` in your settings or by connecting to MCP servers.

<!-- prettier-ignore -->
> [!NOTE]
> For a deep dive into the internal Tool API and how to implement your
> own tools in the codebase, see the `packages/core/src/tools/` directory in
> GitHub.