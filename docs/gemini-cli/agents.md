### `/agents`

- **Description:** Manage local and remote subagents.
- **Note:** This command is experimental and requires
  `experimental.enableAgents: true` in your `settings.json`.
- **Sub-commands:**
  - **`list`**:
    - **Description:** Lists all discovered agents, including built-in, local,
      and remote agents.
    - **Usage:** `/agents list`
  - **`reload`** (alias: `refresh`):
    - **Description:** Rescans agent directories (`~/.gemini/agents` and
      `.gemini/agents`) and reloads the registry.
    - **Usage:** `/agents reload`
  - **`enable`**:
    - **Description:** Enables a specific subagent.
    - **Usage:** `/agents enable <agent-name>`
  - **`disable`**:
    - **Description:** Disables a specific subagent.
    - **Usage:** `/agents disable <agent-name>`
  - **`config`**:
    - **Description:** Opens a configuration dialog for the specified agent to
      adjust its model, temperature, or execution limits.
    - **Usage:** `/agents config <agent-name>`