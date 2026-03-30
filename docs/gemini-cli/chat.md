### `/chat`

- **Description:** Alias for `/resume`. Both commands now expose the same
  session browser action and checkpoint subcommands.
- **Menu layout when typing `/chat` (or `/resume`)**:
  - `-- auto --`
    - `list` (selecting this opens the auto-saved session browser)
  - `-- checkpoints --`
    - `list`, `save`, `resume`, `delete`, `share` (manual tagged checkpoints)
  - Unique prefixes (for example `/cha` or `/resu`) resolve to the same grouped
    menu.
- **Sub-commands:**
  - **`debug`**
    - **Description:** Export the most recent API request as a JSON payload.
  - **`delete <tag>`**
    - **Description:** Deletes a saved conversation checkpoint.
    - **Equivalent:** `/resume delete <tag>`
  - **`list`**
    - **Description:** Lists available tags for manually saved checkpoints.
    - **Note:** This command only lists chats saved within the current project.
      Because chat history is project-scoped, chats saved in other project
      directories will not be displayed.
    - **Equivalent:** `/resume list`
  - **`resume <tag>`**
    - **Description:** Resumes a conversation from a previous save.
    - **Note:** You can only resume chats that were saved within the current
      project. To resume a chat from a different project, you must run the
      Gemini CLI from that project's directory.
    - **Equivalent:** `/resume resume <tag>`
  - **`save <tag>`**
    - **Description:** Saves the current conversation history. You must add a
      `<tag>` for identifying the conversation state.
    - **Details on checkpoint location:** The default locations for saved chat
      checkpoints are:
      - Linux/macOS: `~/.gemini/tmp/<project_hash>/`
      - Windows: `C:\Users\<YourUsername>\.gemini\tmp\<project_hash>\`
      - **Behavior:** Chats are saved into a project-specific directory,
        determined by where you run the CLI. Consequently, saved chats are only
        accessible when working within that same project.
      - **Note:** These checkpoints are for manually saving and resuming
        conversation states. For automatic checkpoints created before file
        modifications, see the
        [Checkpointing documentation](/docs/cli/checkpointing).
      - **Equivalent:** `/resume save <tag>`
  - **`share [filename]`**
    - **Description:** Writes the current conversation to a provided Markdown or
      JSON file. If no filename is provided, then the CLI will generate one.
    - **Usage:** `/chat share file.md` or `/chat share file.json`.
    - **Equivalent:** `/resume share [filename]`