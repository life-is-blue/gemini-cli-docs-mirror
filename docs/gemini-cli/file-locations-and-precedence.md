## File locations and precedence

Gemini CLI discovers commands from two locations, loaded in a specific order:

1.  **User commands (global):** Located in `~/.gemini/commands/`. These commands
    are available in any project you are working on.
2.  **Project commands (local):** Located in
    `<your-project-root>/.gemini/commands/`. These commands are specific to the
    current project and can be checked into version control to be shared with
    your team.

If a command in the project directory has the same name as a command in the user
directory, the **project command will always be used.** This allows projects to
override global commands with project-specific versions.