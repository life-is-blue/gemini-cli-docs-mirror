## Highlights

- **Customizable Keyboard Shortcuts:** Significant improvements to input
  flexibility with support for custom keybindings, literal character bindings,
  and extended terminal protocol keys.
- **Vim Mode Enhancements:** Further refinement of the Vim modal editing
  experience, adding common motions like \`X\`, \`~\`, \`r\`, and \`f/F/t/T\`,
  along with yank and paste support.
- **Enhanced Security through Sandboxing:** Introduction of a unified
  \`SandboxManager\` and integration of Linux-native sandboxing (bubblewrap and
  seccomp) to isolate tool execution and improve system security.
- **JIT Context Discovery:** Improved performance and accuracy by enabling
  Just-In-Time context loading for file system tools, ensuring the model has the
  most relevant information without overwhelming the context.
- **Subagent & Performance Updates:** Subagents are now enabled by default,
  supported by a model-driven parallel tool scheduler and code splitting for
  faster startup and more efficient task execution.