### Scenario: Using the hierarchy

Context is loaded hierarchically. This allows you to have general rules for
everything and specific rules for sub-projects.

1.  **Global:** `~/.gemini/GEMINI.md` (Rules for _every_ project you work on).
2.  **Project Root:** `./GEMINI.md` (Rules for the current repository).
3.  **Subdirectory:** `./src/GEMINI.md` (Rules specific to the `src` folder).

**Example:** You might set "Always use strict typing" in your global config, but
"Use Python 3.11" only in your backend repository.