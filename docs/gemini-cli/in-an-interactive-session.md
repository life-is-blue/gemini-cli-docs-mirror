### In an Interactive Session

Use the `/skills` slash command to view and manage available expertise:

- `/skills list` (default): Shows all discovered skills and their status.
- `/skills link <path>`: Links agent skills from a local directory via symlink.
- `/skills disable <name>`: Prevents a specific skill from being used.
- `/skills enable <name>`: Re-enables a disabled skill.
- `/skills reload`: Refreshes the list of discovered skills from all tiers.

<!-- prettier-ignore -->
> [!NOTE]
> `/skills disable` and `/skills enable` default to the `user` scope. Use
> `--scope workspace` to manage workspace-specific settings.