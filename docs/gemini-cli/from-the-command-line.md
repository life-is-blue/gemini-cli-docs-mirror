### From the command line

When starting Gemini CLI, use the `--resume` (or `-r`) flag to load existing
sessions.

- **Resume latest:**

  ```bash
  gemini --resume
  ```

  This immediately loads the most recent session.

- **Resume by index:** List available sessions first (see
  [Listing sessions](#listing-sessions)), then use the index number:

  ```bash
  gemini --resume 1
  ```

- **Resume by ID:** You can also provide the full session UUID:
  ```bash
  gemini --resume a1b2c3d4-e5f6-7890-abcd-ef1234567890
  ```