### `/copy`

- **Description:** Copies the last output produced by Gemini CLI to your
  clipboard, for easy sharing or reuse.
- **Behavior:**
  - Local sessions use system clipboard tools (pbcopy/xclip/clip).
  - Remote sessions (SSH/WSL) use OSC 52 and require terminal support.
- **Note:** This command requires platform-specific clipboard tools to be
  installed.
  - On Linux, it requires `xclip` or `xsel`. You can typically install them
    using your system's package manager.
  - On macOS, it requires `pbcopy`, and on Windows, it requires `clip`. These
    tools are typically pre-installed on their respective systems.