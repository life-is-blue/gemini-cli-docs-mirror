### From the interactive interface

While the CLI is running, use the `/resume` slash command to open the **Session
Browser**:

```text
/resume
```

When typing `/resume` (or `/chat`) in slash completion, commands are grouped
under titled separators:

- `-- auto --` (session browser)
  - `list` is selectable and opens the session browser
- `-- checkpoints --` (manual tagged checkpoint commands)

Unique prefixes such as `/resum` and `/cha` resolve to the same grouped menu.

The Session Browser provides an interactive interface where you can perform the
following actions:

- **Browse:** Scroll through a list of your past sessions.
- **Preview:** See details like the session date, message count, and the first
  user prompt.
- **Search:** Press `/` to enter search mode, then type to filter sessions by ID
  or content.
- **Select:** Press **Enter** to resume the selected session.
- **Esc:** Press **Esc** to exit the Session Browser.