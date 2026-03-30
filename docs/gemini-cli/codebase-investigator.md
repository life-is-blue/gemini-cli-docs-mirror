### Codebase Investigator

- **Name:** `codebase_investigator`
- **Purpose:** Analyze the codebase, reverse engineer, and understand complex
  dependencies.
- **When to use:** "How does the authentication system work?", "Map out the
  dependencies of the `AgentRegistry` class."
- **Configuration:** Enabled by default. You can override its settings in
  `settings.json` under `agents.overrides`. Example (forcing a specific model
  and increasing turns):
  ```json
  {
    "agents": {
      "overrides": {
        "codebase_investigator": {
          "modelConfig": { "model": "gemini-3-flash-preview" },
          "runConfig": { "maxTurns": 50 }
        }
      }
    }
  }
  ```