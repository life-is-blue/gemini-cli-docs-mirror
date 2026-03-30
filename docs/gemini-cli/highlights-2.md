## Highlights

- **Subagent Architecture Enhancements:** Significant updates to subagents,
  including local execution, tool isolation, multi-registry discovery, dynamic
  tool filtering, and JIT context injection.
- **Enhanced Security & Sandboxing:** Implemented strict macOS sandboxing using
  Seatbelt allowlist, native Windows sandboxing, and support for
  "Write-Protected" governance files.
- **Agent Context & State Management:** Introduced task tracker protocol
  integration, 'blocked' statuses for tasks/todos, and `AgentSession` for
  improved state management and replay semantics.
- **Browser & ACP Capabilities:** Added privacy consent for the browser agent,
  sensitive action controls, improved API token usage metadata, and gateway auth
  support via ACP.
- **CLI & UX Improvements:** Implemented a refreshed Composer layout, expanded
  terminal fallback warnings, dynamic model resolution, and Git worktree support
  for isolated parallel sessions.