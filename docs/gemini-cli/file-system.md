### File System

| Tool                                         | Kind     | Description                                                                                           |
| :------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------- |
| [`glob`](/docs/tools/file-system)            | `Search` | Finds files matching specific glob patterns across the workspace.                                     |
| [`grep_search`](/docs/tools/file-system)     | `Search` | Searches for a regular expression pattern within file contents. Legacy alias: `search_file_content`.  |
| [`list_directory`](/docs/tools/file-system)  | `Read`   | Lists the names of files and subdirectories within a specified path.                                  |
| [`read_file`](/docs/tools/file-system)       | `Read`   | Reads the content of a specific file. Supports text, images, audio, and PDF.                          |
| [`read_many_files`](/docs/tools/file-system) | `Read`   | Reads and concatenates content from multiple files. Often triggered by the `@` symbol in your prompt. |
| [`replace`](/docs/tools/file-system)         | `Edit`   | Performs precise text replacement within a file. Requires manual confirmation.                        |
| [`write_file`](/docs/tools/file-system)      | `Edit`   | Creates or overwrites a file with new content. Requires manual confirmation.                          |