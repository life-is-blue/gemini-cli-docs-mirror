### 4. Injecting file content with `@{...}`

You can directly embed the content of a file or a directory listing into your
prompt using the `@{...}` syntax. This is useful for creating commands that
operate on specific files.

**How it works:**

- **File injection**: `@{path/to/file.txt}` is replaced by the content of
  `file.txt`.
- **Multimodal support**: If the path points to a supported image (e.g., PNG,
  JPEG), PDF, audio, or video file, it will be correctly encoded and injected as
  multimodal input. Other binary files are handled gracefully and skipped.
- **Directory listing**: `@{path/to/dir}` is traversed and each file present
  within the directory and all subdirectories is inserted into the prompt. This
  respects `.gitignore` and `.geminiignore` if enabled.
- **Workspace-aware**: The command searches for the path in the current
  directory and any other workspace directories. Absolute paths are allowed if
  they are within the workspace.
- **Processing order**: File content injection with `@{...}` is processed
  _before_ shell commands (`!{...}`) and argument substitution (`{{args}}`).
- **Parsing**: The parser requires the content inside `@{...}` (the path) to
  have balanced braces (`{` and `}`).

**Example (`review.toml`):**

This command injects the content of a _fixed_ best practices file
(`docs/best-practices.md`) and uses the user's arguments to provide context for
the review.

```toml