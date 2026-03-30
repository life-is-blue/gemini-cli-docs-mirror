## Memory discovery service

The memory discovery service is responsible for finding and loading the
`GEMINI.md` files that provide context to the model. It searches for these files
in a hierarchical manner, starting from the current working directory and moving
up to the project root and the user's home directory. It also searches in
subdirectories.

This allows you to have global, project-level, and component-level context
files, which are all combined to provide the model with the most relevant
information.

You can use the [`/memory` command](/docs/reference/commands) to `show`, `add`,
and `refresh` the content of loaded `GEMINI.md` files.