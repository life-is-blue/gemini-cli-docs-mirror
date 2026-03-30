## Interactive commands

The `run_shell_command` tool now supports interactive commands by integrating a
pseudo-terminal (pty). This allows you to run commands that require real-time
user input, such as text editors (`vim`, `nano`), terminal-based UIs (`htop`),
and interactive version control operations (`git rebase -i`).

When an interactive command is running, you can send input to it from the Gemini
CLI. To focus on the interactive shell, press `Tab`. The terminal output,
including complex TUIs, will be rendered correctly.