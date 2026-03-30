## Security and risks

<!-- prettier-ignore -->
> [!WARNING]
> Hooks execute arbitrary code with your user privileges. By
> configuring hooks, you are allowing scripts to run shell commands on your
> machine.

**Project-level hooks** are particularly risky when opening untrusted projects.
Gemini CLI **fingerprints** project hooks. If a hook's name or command changes
(e.g., via `git pull`), it is treated as a **new, untrusted hook** and you will
be warned before it executes.

See [Security Considerations](/docs/hooks/best-practices#using-hooks-securely) for
a detailed threat model.