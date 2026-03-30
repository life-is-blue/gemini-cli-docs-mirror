## Tool Restrictions

Plan Mode enforces strict safety policies to prevent accidental changes.

These are the only allowed tools:

- **FileSystem (Read):**
  [`read_file`](/docs/tools/file-system#2-read_file-readfile),
  [`list_directory`](/docs/tools/file-system#1-list_directory-readfolder),
  [`glob`](/docs/tools/file-system#4-glob-findfiles)
- **Search:** [`grep_search`](/docs/tools/file-system#5-grep_search-searchtext),
  [`google_web_search`](/docs/tools/web-search),
  [`get_internal_docs`](/docs/tools/internal-docs)
- **Research Subagents:**
  [`codebase_investigator`](/docs/core/subagents#codebase-investigator),
  [`cli_help`](/docs/core/subagents#cli-help-agent)
- **Interaction:** [`ask_user`](/docs/tools/ask-user)
- **MCP tools (Read):** Read-only [MCP tools](/docs/tools/mcp-server) (for
  example, `github_read_issue`, `postgres_read_schema`) are allowed.
- **Planning (Write):**
  [`write_file`](/docs/tools/file-system#3-write_file-writefile) and
  [`replace`](/docs/tools/file-system#6-replace-edit) only allowed for `.md`
  files in the `~/.gemini/tmp/<project>/<session-id>/plans/` directory or your
  [custom plans directory](#custom-plan-directory-and-policies).
- **Memory:** [`save_memory`](/docs/tools/memory)
- **Skills:** [`activate_skill`](/docs/cli/skills) (allows loading specialized
  instructions and resources in a read-only manner)