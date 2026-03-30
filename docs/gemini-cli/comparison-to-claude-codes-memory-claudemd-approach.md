## Comparison to Claude Code's `/memory` (`claude.md`) approach

Claude Code's `/memory` feature (as seen in `claude.md`) produces a flat, linear
document by concatenating all included files, always marking file boundaries
with clear comments and path names. It does not explicitly present the import
hierarchy, but the LLM receives all file contents and paths, which is sufficient
for reconstructing the hierarchy if needed.

> [!NOTE] The import tree is mainly for clarity during development and has
> limited relevance to LLM consumption.