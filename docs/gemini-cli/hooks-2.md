### `/hooks`

- **Description:** Manage hooks, which allow you to intercept and customize
  Gemini CLI behavior at specific lifecycle events.
- **Sub-commands:**
  - **`disable-all`**:
    - **Description:** Disable all enabled hooks.
  - **`disable <hook-name>`**:
    - **Description:** Disable a hook by name.
  - **`enable-all`**:
    - **Description:** Enable all disabled hooks.
  - **`enable <hook-name>`**:
    - **Description:** Enable a hook by name.
  - **`list`** (or `show`, `panel`):
    - **Description:** Display all registered hooks with their status.