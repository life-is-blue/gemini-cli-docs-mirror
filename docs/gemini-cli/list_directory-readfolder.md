### `list_directory` (ReadFolder)

Lists the names of files and subdirectories directly within a specified path.

- **Tool name:** `list_directory`
- **Arguments:**
  - `dir_path` (string, required): Absolute or relative path to the directory.
  - `ignore` (array, optional): Glob patterns to exclude.
  - `file_filtering_options` (object, optional): Configuration for `.gitignore`
    and `.geminiignore` compliance.