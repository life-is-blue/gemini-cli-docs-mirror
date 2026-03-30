### `replace` (Edit)

`replace` replaces text within a file. By default, the tool expects to find and
replace exactly ONE occurrence of `old_string`. If you want to replace multiple
occurrences of the exact same string, set `allow_multiple` to `true`. This tool
is designed for precise, targeted changes and requires significant context
around the `old_string` to ensure it modifies the correct location.

- **Tool name:** `replace`
- **Arguments:**
  - `file_path` (string, required): Path to the file.
  - `instruction` (string, required): Semantic description of the change.
  - `old_string` (string, required): Exact literal text to find.
  - `new_string` (string, required): Exact literal text to replace with.
  - `allow_multiple` (boolean, optional): If `true`, replaces all occurrences.
    If `false` (default), only succeeds if exactly one occurrence is found.
- **Confirmation:** Requires manual user approval.