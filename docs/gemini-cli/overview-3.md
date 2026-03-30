## Overview

The `GEMINI_SYSTEM_MD` variable instructs the CLI to use an external Markdown
file for its system prompt, completely overriding the built-in default. This is
a full replacement, not a merge. If you use a custom file, none of the original
core instructions will apply unless you include them yourself.

This feature is intended for advanced users who need to enforce strict,
project-specific behavior or create a customized persona.

<!-- prettier-ignore -->
> [!TIP]
> You can export the current default system prompt to a file first, review
> it, and then selectively modify or replace it (see
> [“Export the default prompt”](#export-the-default-prompt-recommended)).