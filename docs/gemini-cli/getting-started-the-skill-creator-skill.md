## Getting started: The `skill-creator` skill

The recommended way to create a new skill is to use the built-in `skill-creator`
skill. To use it, ask Gemini CLI to create a new skill for you.

**Example prompt:**

> "create a new skill called 'code-reviewer'"

Gemini CLI will then use the `skill-creator` to generate the skill:

1.  Generate a new directory for your skill (e.g., `my-new-skill/`).
2.  Create a `SKILL.md` file with the necessary YAML frontmatter (`name` and
    `description`).
3.  Create the standard resource directories: `scripts/`, `references/`, and
    `assets/`.