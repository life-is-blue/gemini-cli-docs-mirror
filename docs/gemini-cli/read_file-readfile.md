### `read_file` (ReadFile)

Reads and returns the content of a specific file. Supports text, images, audio,
and PDF.

- **Tool name:** `read_file`
- **Arguments:**
  - `file_path` (string, required): Path to the file.
  - `offset` (number, optional): Start line for text files (0-based).
  - `limit` (number, optional): Maximum lines to read.