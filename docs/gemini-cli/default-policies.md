## Default policies

The Gemini CLI ships with a set of default policies to provide a safe
out-of-the-box experience.

- **Read-only tools** (like `read_file`, `glob`) are generally **allowed**.
- **Agent delegation** defaults to **`ask_user`** to ensure remote agents can
  prompt for confirmation, but local sub-agent actions are executed silently and
  checked individually.
- **Write tools** (like `write_file`, `run_shell_command`) default to
  **`ask_user`**.
- In **`yolo`** mode, a high-priority rule allows all tools.
- In **`autoEdit`** mode, rules allow certain write operations to happen without
  prompting.