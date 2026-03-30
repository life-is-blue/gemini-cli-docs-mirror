### Command restrictions

You can limit which commands the agent is allowed to request using these
settings:

- **`tools.core`**: An allowlist of command prefixes (for example,
  `["git", "npm test"]`).
- **`tools.exclude`**: A blocklist of command prefixes.