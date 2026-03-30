### `glob` (FindFiles)

Finds files matching specific glob patterns across the workspace.

- **Tool name:** `glob`
- **Display name:** FindFiles
- **File:** `glob.ts`
- **Parameters:**
  - `pattern` (string, required): The glob pattern to match against (e.g.,
    `"*.py"`, `"src/**/*.js"`).
  - `path` (string, optional): The absolute path to the directory to search
    within. If omitted, searches the tool's root directory.
  - `case_sensitive` (boolean, optional): Whether the search should be
    case-sensitive. Defaults to `false`.
  - `respect_git_ignore` (boolean, optional): Whether to respect .gitignore
    patterns when finding files. Defaults to `true`.
- **Behavior:**
  - Searches for files matching the glob pattern within the specified directory.
  - Returns a list of absolute paths, sorted with the most recently modified
    files first.
  - Ignores common nuisance directories like `node_modules` and `.git` by
    default.
- **Output (`llmContent`):** A message like:
  `Found 5 file(s) matching "*.ts" within src, sorted by modification time (newest first):\nsrc/file1.ts\nsrc/subdir/file2.ts...`
- **Confirmation:** No.