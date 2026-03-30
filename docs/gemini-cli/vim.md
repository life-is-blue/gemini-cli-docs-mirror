### `/vim`

- **Description:** Toggle vim mode on or off. When vim mode is enabled, the
  input area supports vim-style navigation and editing commands in both NORMAL
  and INSERT modes.
- **Features:**
  - **Count support:** Prefix commands with numbers (e.g., `3h`, `5w`, `10G`)
  - **Editing commands:** Delete with `x`, change with `c`, insert with `i`,
    `a`, `o`, `O`; complex operations like `dd`, `cc`, `dw`, `cw`
  - **INSERT mode:** Standard text input with escape to return to NORMAL mode
  - **NORMAL mode:** Navigate with `h`, `j`, `k`, `l`; jump by words with `w`,
    `b`, `e`; go to line start/end with `0`, `$`, `^`; go to specific lines with
    `G` (or `gg` for first line)
  - **Persistent setting:** Vim mode preference is saved to
    `~/.gemini/settings.json` and restored between sessions
  - **Repeat last command:** Use `.` to repeat the last editing operation
  - **Status indicator:** When enabled, shows `[NORMAL]` or `[INSERT]` in the
    footer