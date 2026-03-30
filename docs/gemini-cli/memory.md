### `/memory`

- **Description:** Manage the AI's instructional context (hierarchical memory
  loaded from `GEMINI.md` files).
- **Sub-commands:**
  - **`add`**:
    - **Description:** Adds the following text to the AI's memory. Usage:
      `/memory add <text to remember>`
  - **`list`**:
    - **Description:** Lists the paths of the GEMINI.md files in use for
      hierarchical memory.
  - **`refresh`**:
    - **Description:** Reload the hierarchical instructional memory from all
      `GEMINI.md` files found in the configured locations (global,
      project/ancestors, and sub-directories). This command updates the model
      with the latest `GEMINI.md` content.
  - **`show`**:
    - **Description:** Display the full, concatenated content of the current
      hierarchical memory that has been loaded from all `GEMINI.md` files. This
      lets you inspect the instructional context being provided to the Gemini
      model.
  - **Note:** For more details on how `GEMINI.md` files contribute to
    hierarchical memory, see the
    [CLI Configuration documentation](/docs/reference/configuration).