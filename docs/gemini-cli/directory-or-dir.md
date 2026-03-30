### `/directory` (or `/dir`)

- **Description:** Manage workspace directories for multi-directory support.
- **Sub-commands:**
  - **`add`**:
    - **Description:** Add a directory to the workspace. The path can be
      absolute or relative to the current working directory. Moreover, the
      reference from home directory is supported as well.
    - **Usage:** `/directory add <path1>,<path2>`
    - **Note:** Disabled in restrictive sandbox profiles. If you're using that,
      use `--include-directories` when starting the session instead.
  - **`show`**:
    - **Description:** Display all directories added by `/directory add` and
      `--include-directories`.
    - **Usage:** `/directory show`