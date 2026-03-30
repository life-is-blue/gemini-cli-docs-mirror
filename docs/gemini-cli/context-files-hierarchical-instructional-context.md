## Context files (hierarchical instructional context)

While not strictly configuration for the CLI's _behavior_, context files
(defaulting to `GEMINI.md` but configurable via the `context.fileName` setting)
are crucial for configuring the _instructional context_ (also referred to as
"memory") provided to the Gemini model. This powerful feature allows you to give
project-specific instructions, coding style guides, or any relevant background
information to the AI, making its responses more tailored and accurate to your
needs. The CLI includes UI elements, such as an indicator in the footer showing
the number of loaded context files, to keep you informed about the active
context.

- **Purpose:** These Markdown files contain instructions, guidelines, or context
  that you want the Gemini model to be aware of during your interactions. The
  system is designed to manage this instructional context hierarchically.