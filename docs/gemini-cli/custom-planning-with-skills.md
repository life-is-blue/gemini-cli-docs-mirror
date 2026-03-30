### Custom planning with skills

You can use [Agent Skills](/docs/cli/skills) to customize how Gemini CLI
approaches planning for specific types of tasks. When a skill is activated
during Plan Mode, its specialized instructions and procedural workflows will
guide the research, design, and planning phases.

For example:

- A **"Database Migration"** skill could ensure the plan includes data safety
  checks and rollback strategies.
- A **"Security Audit"** skill could prompt Gemini CLI to look for specific
  vulnerabilities during codebase exploration.
- A **"Frontend Design"** skill could guide Gemini CLI to use specific UI
  components and accessibility standards in its proposal.

To use a skill in Plan Mode, you can explicitly ask Gemini CLI to "use the
`<skill-name>` skill to plan..." or Gemini CLI may autonomously activate it
based on the task description.