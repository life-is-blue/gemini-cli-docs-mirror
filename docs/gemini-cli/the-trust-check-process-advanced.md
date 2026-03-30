## The trust check process (advanced)

For advanced users, it's helpful to know the exact order of operations for how
trust is determined:

1.  **IDE trust signal**: If you are using the
    [IDE Integration](/docs/ide-integration), the CLI first asks the IDE
    if the workspace is trusted. The IDE's response takes highest priority.

2.  **Local trust file**: If the IDE is not connected, the CLI checks the
    central `~/.gemini/trustedFolders.json` file.