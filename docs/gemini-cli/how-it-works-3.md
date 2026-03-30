## How it works

When you approve a tool that modifies the file system (like `write_file` or
`replace`), the CLI automatically creates a "checkpoint." This checkpoint
includes:

1.  **A Git snapshot:** A commit is made in a special, shadow Git repository
    located in your home directory (`~/.gemini/history/<project_hash>`). This
    snapshot captures the complete state of your project files at that moment.
    It does **not** interfere with your own project's Git repository.
2.  **Conversation history:** The entire conversation you've had with the agent
    up to that point is saved.
3.  **The tool call:** The specific tool call that was about to be executed is
    also stored.

If you want to undo the change or simply go back, you can use the `/restore`
command. Restoring a checkpoint will:

- Revert all files in your project to the state captured in the snapshot.
- Restore the conversation history in the CLI.
- Re-propose the original tool call, allowing you to run it again, modify it, or
  simply ignore it.

All checkpoint data, including the Git snapshot and conversation history, is
stored locally on your machine. The Git snapshot is stored in the shadow
repository while the conversation history and tool calls are saved in a JSON
file in your project's temporary directory, typically located at
`~/.gemini/tmp/<project_hash>/checkpoints`.