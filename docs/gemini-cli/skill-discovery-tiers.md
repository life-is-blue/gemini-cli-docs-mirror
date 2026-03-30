## Skill Discovery Tiers

Gemini CLI discovers skills from three primary locations:

1.  **Workspace Skills**: Located in `.gemini/skills/` or the `.agents/skills/`
    alias. Workspace skills are typically committed to version control and
    shared with the team.
2.  **User Skills**: Located in `~/.gemini/skills/` or the `~/.agents/skills/`
    alias. These are personal skills available across all your workspaces.
3.  **Extension Skills**: Skills bundled within installed
    [extensions](/docs/extensions).

**Precedence:** If multiple skills share the same name, higher-precedence
locations override lower ones: **Workspace > User > Extension**.

Within the same tier (user or workspace), the `.agents/skills/` alias takes
precedence over the `.gemini/skills/` directory. This generic alias provides an
intuitive path for managing agent-specific expertise that remains compatible
across different AI agent tools.