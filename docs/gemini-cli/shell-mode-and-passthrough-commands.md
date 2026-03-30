## Shell mode and passthrough commands (`!`)

The `!` prefix lets you interact with your system's shell directly from within
Gemini CLI.

- **`!<shell_command>`**
  - **Description:** Execute the given `<shell_command>` using `bash` on
    Linux/macOS or `powershell.exe -NoProfile -Command` on Windows (unless you
    override `ComSpec`). Any output or errors from the command are displayed in
    the terminal.
  - **Examples:**
    - `!ls -la` (executes `ls -la` and returns to Gemini CLI)
    - `!git status` (executes `git status` and returns to Gemini CLI)

- **`!` (Toggle shell mode)**
  - **Description:** Typing `!` on its own toggles shell mode.
    - **Entering shell mode:**
      - When active, shell mode uses a different coloring and a "Shell Mode
        Indicator".
      - While in shell mode, text you type is interpreted directly as a shell
        command.
    - **Exiting shell mode:**
      - When exited, the UI reverts to its standard appearance and normal Gemini
        CLI behavior resumes.

- **Caution for all `!` usage:** Commands you execute in shell mode have the
  same permissions and impact as if you ran them directly in your terminal.

- **Environment variable:** When a command is executed via `!` or in shell mode,
  the `GEMINI_CLI=1` environment variable is set in the subprocess's
  environment. This allows scripts or tools to detect if they are being run from
  within the Gemini CLI.