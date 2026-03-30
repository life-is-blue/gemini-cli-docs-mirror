## Shell history

The CLI keeps a history of shell commands you run. To avoid conflicts between
different projects, this history is stored in a project-specific directory
within your user's home folder.

- **Location:** `~/.gemini/tmp/<project_hash>/shell_history`
  - `<project_hash>` is a unique identifier generated from your project's root
    path.
  - The history is stored in a file named `shell_history`.