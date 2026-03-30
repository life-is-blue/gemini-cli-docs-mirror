### `/resume`

- **Description:** Browse and resume previous conversation sessions, and manage
  manual chat checkpoints.
- **Features:**
  - **Auto sessions:** Run `/resume` to open the interactive session browser for
    automatically saved conversations.
  - **Chat checkpoints:** Use checkpoint subcommands directly (`/resume save`,
    `/resume resume`, etc.).
  - **Management:** Delete unwanted sessions directly from the browser
  - **Resume:** Select any session to resume and continue the conversation
  - **Search:** Use `/` to search through conversation content across all
    sessions
  - **Session Browser:** Interactive interface showing all saved sessions with
    timestamps, message counts, and first user message for context
  - **Sorting:** Sort sessions by date or message count
- **Note:** All conversations are automatically saved as you chat - no manual
  saving required. See [Session Management](/docs/cli/session-management) for
  complete details.
- **Alias:** `/chat` provides the same behavior and subcommands.
- **Sub-commands:**
  - **`list`**
    - **Description:** Lists available tags for manual chat checkpoints.
  - **`save <tag>`**
    - **Description:** Saves the current conversation as a tagged checkpoint.
  - **`resume <tag>`** (alias: `load`)
    - **Description:** Loads a previously saved tagged checkpoint.
  - **`delete <tag>`**
    - **Description:** Deletes a tagged checkpoint.
  - **`share [filename]`**
    - **Description:** Exports the current conversation to Markdown or JSON.
  - **`debug`**
    - **Description:** Export the most recent API request as JSON payload
      (nightly builds).
  - **Compatibility alias:** `/resume checkpoints ...` is still accepted for the
    same checkpoint commands.