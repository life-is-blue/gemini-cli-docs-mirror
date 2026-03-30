### Priority system and tiers

The policy engine uses a sophisticated priority system to resolve conflicts when
multiple rules match a single tool call. The core principle is simple: **the
rule with the highest priority wins**.

To provide a clear hierarchy, policies are organized into three tiers. Each tier
has a designated number that forms the base of the final priority calculation.

| Tier      | Base | Description                                                                |
| :-------- | :--- | :------------------------------------------------------------------------- |
| Default   | 1    | Built-in policies that ship with the Gemini CLI.                           |
| Extension | 2    | Policies defined in extensions.                                            |
| Workspace | 3    | Policies defined in the current workspace's configuration directory.       |
| User      | 4    | Custom policies defined by the user.                                       |
| Admin     | 5    | Policies managed by an administrator (e.g., in an enterprise environment). |

Within a TOML policy file, you assign a priority value from **0 to 999**. The
engine transforms this into a final priority using the following formula:

`final_priority = tier_base + (toml_priority / 1000)`

This system guarantees that:

- Admin policies always override User, Workspace, and Default policies.
- User policies override Workspace and Default policies.
- Workspace policies override Default policies.
- You can still order rules within a single tier with fine-grained control.

For example:

- A `priority: 50` rule in a Default policy file becomes `1.050`.
- A `priority: 10` rule in a Workspace policy policy file becomes `2.010`.
- A `priority: 100` rule in a User policy file becomes `3.100`.
- A `priority: 20` rule in an Admin policy file becomes `4.020`.