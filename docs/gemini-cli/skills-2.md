### `/skills`

- **Description:** Manage Agent Skills, which provide on-demand expertise and
  specialized workflows.
- **Sub-commands:**
  - **`disable <name>`**:
    - **Description:** Disable a specific skill by name.
    - **Usage:** `/skills disable <name>`
  - **`enable <name>`**:
    - **Description:** Enable a specific skill by name.
    - **Usage:** `/skills enable <name>`
  - **`list`**:
    - **Description:** List all discovered skills and their current status
      (enabled/disabled).
  - **`reload`**:
    - **Description:** Refresh the list of discovered skills from all tiers
      (workspace, user, and extensions).