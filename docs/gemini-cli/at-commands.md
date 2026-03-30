## At commands (`@`)

At commands are used to include the content of files or directories as part of
your prompt to Gemini. These commands include git-aware filtering.

- **`@<path_to_file_or_directory>`**
  - **Description:** Inject the content of the specified file or files into your
    current prompt. This is useful for asking questions about specific code,
    text, or collections of files.
  - **Examples:**
    - `@path/to/your/file.txt Explain this text.`
    - `@src/my_project/ Summarize the code in this directory.`
    - `What is this file about? @README.md`
  - **Details:**
    - If a path to a single file is provided, the content of that file is read.
    - If a path to a directory is provided, the command attempts to read the
      content of files within that directory and any subdirectories.
    - Spaces in paths should be escaped with a backslash (e.g.,
      `@My\ Documents/file.txt`).
    - The command uses the `read_many_files` tool internally. The content is
      fetched and then inserted into your query before being sent to the Gemini
      model.
    - **Git-aware filtering:** By default, git-ignored files (like
      `node_modules/`, `dist/`, `.env`, `.git/`) are excluded. This behavior can
      be changed via the `context.fileFiltering` settings.
    - **File types:** The command is intended for text-based files. While it
      might attempt to read any file, binary files or very large files might be
      skipped or truncated by the underlying `read_many_files` tool to ensure
      performance and relevance. The tool indicates if files were skipped.
  - **Output:** The CLI will show a tool call message indicating that
    `read_many_files` was used, along with a message detailing the status and
    the path(s) that were processed.

- **`@` (Lone at symbol)**
  - **Description:** If you type a lone `@` symbol without a path, the query is
    passed as-is to the Gemini model. This might be useful if you are
    specifically talking _about_ the `@` symbol in your prompt.