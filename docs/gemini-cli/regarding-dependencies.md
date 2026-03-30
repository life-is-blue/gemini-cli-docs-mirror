## Regarding Dependencies:

- Avoid introducing new external dependencies unless absolutely necessary.
- If a new dependency is required, please state the reason.
```

This example demonstrates how you can provide general project context, specific
coding conventions, and even notes about particular files or components. The
more relevant and precise your context files are, the better the AI can assist
you. Project-specific context files are highly encouraged to establish
conventions and context.

- **Hierarchical loading and precedence:** The CLI implements a sophisticated
  hierarchical memory system by loading context files (e.g., `GEMINI.md`) from
  several locations. Content from files lower in this list (more specific)
  typically overrides or supplements content from files higher up (more
  general). The exact concatenation order and final context can be inspected
  using the `/memory show` command. The typical loading order is:
  1.  **Global context file:**
      - Location: `~/.gemini/<configured-context-filename>` (e.g.,
        `~/.gemini/GEMINI.md` in your user home directory).
      - Scope: Provides default instructions for all your projects.
  2.  **Project root and ancestors context files:**
      - Location: The CLI searches for the configured context file in the
        current working directory and then in each parent directory up to either
        the project root (identified by a `.git` folder) or your home directory.
      - Scope: Provides context relevant to the entire project or a significant
        portion of it.
  3.  **Sub-directory context files (contextual/local):**
      - Location: The CLI also scans for the configured context file in
        subdirectories _below_ the current working directory (respecting common
        ignore patterns like `node_modules`, `.git`, etc.). The breadth of this
        search is limited to 200 directories by default, but can be configured
        with the `context.discoveryMaxDirs` setting in your `settings.json`
        file.
      - Scope: Allows for highly specific instructions relevant to a particular
        component, module, or subsection of your project.
- **Concatenation and UI indication:** The contents of all found context files
  are concatenated (with separators indicating their origin and path) and
  provided as part of the system prompt to the Gemini model. The CLI footer
  displays the count of loaded context files, giving you a quick visual cue
  about the active instructional context.
- **Importing content:** You can modularize your context files by importing
  other Markdown files using the `@path/to/file.md` syntax. For more details,
  see the [Memory Import Processor documentation](/docs/reference/memport).
- **Commands for memory management:**
  - Use `/memory refresh` to force a re-scan and reload of all context files
    from all configured locations. This updates the AI's instructional context.
  - Use `/memory show` to display the combined instructional context currently
    loaded, allowing you to verify the hierarchy and content being used by the
    AI.
  - See the [Commands documentation](/docs/reference/commands#memory) for full details on
    the `/memory` command and its sub-commands (`show` and `reload`).

By understanding and utilizing these configuration layers and the hierarchical
nature of context files, you can effectively manage the AI's memory and tailor
the Gemini CLI's responses to your specific needs and projects.