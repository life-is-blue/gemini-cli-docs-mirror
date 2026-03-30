### Threat Model

Understanding where hooks come from and what they can do is critical for secure
usage.

| Hook Source                   | Description                                                                                                                |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **System**                    | Configured by system administrators (e.g., `/etc/gemini-cli/settings.json`, `/Library/...`). Assumed to be the **safest**. |
| **User** (`~/.gemini/...`)    | Configured by you. You are responsible for ensuring they are safe.                                                         |
| **Extensions**                | You explicitly approve and install these. Security depends on the extension source (integrity).                            |
| **Project** (`./.gemini/...`) | **Untrusted by default.** Safest in trusted internal repos; higher risk in third-party/public repos.                       |

#### Project Hook Security

When you open a project with hooks defined in `.gemini/settings.json`:

1. **Detection**: Gemini CLI detects the hooks.
2. **Identification**: A unique identity is generated for each hook based on its
   `name` and `command`.
3. **Warning**: If this specific hook identity has not been seen before, a
   **warning** is displayed.
4. **Execution**: The hook is executed (unless specific security settings block
   it).
5. **Trust**: The hook is marked as "trusted" for this project.

> **Modification detection**: If the `command` string of a project hook is
> changed (e.g., by a `git pull`), its identity changes. Gemini CLI will treat
> it as a **new, untrusted hook** and warn you again. This prevents malicious
> actors from silently swapping a verified command for a malicious one.