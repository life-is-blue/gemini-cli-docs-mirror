### `grep_search` (SearchText)

`grep_search` searches for a regular expression pattern within the content of
files in a specified directory. Can filter files by a glob pattern. Returns the
lines containing matches, along with their file paths and line numbers.

- **Tool name:** `grep_search`
- **Display name:** SearchText
- **File:** `grep.ts`
- **Parameters:**
  - `pattern` (string, required): The regular expression (regex) to search for
    (e.g., `"function\s+myFunction"`).
  - `path` (string, optional): The absolute path to the directory to search
    within. Defaults to the current working directory.
  - `include` (string, optional): A glob pattern to filter which files are
    searched (e.g., `"*.js"`, `"src/**/*.{ts,tsx}"`). If omitted, searches most
    files (respecting common ignores).
- **Behavior:**
  - Uses `git grep` if available in a Git repository for speed; otherwise, falls
    back to system `grep` or a JavaScript-based search.
  - Returns a list of matching lines, each prefixed with its file path (relative
    to the search directory) and line number.
- **Output (`llmContent`):** A formatted string of matches, e.g.:
  ```
  Found 3 matches for pattern "myFunction" in path "." (filter: "*.ts"):
  ---
  File: src/utils.ts
  L15: export function myFunction() {
  L22:   myFunction.call();
  ---
  File: src/index.ts
  L5: import { myFunction } from './utils';
  ---
  ```
- **Confirmation:** No.