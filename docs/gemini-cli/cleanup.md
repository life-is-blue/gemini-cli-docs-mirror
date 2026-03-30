## Cleanup

By default, Gemini CLI automatically cleans up old session data, including all
associated plan files and task trackers.

- **Default behavior:** Sessions (and their plans) are retained for **30 days**.
- **Configuration:** You can customize this behavior via the `/settings` command
  (search for **Session Retention**) or in your `settings.json` file. See
  [session retention](/docs/cli/session-management#session-retention) for more
  details.

Manual deletion also removes all associated artifacts:

- **Command Line:** Use `gemini --delete-session <index|id>`.
- **Session Browser:** Press `/resume`, navigate to a session, and press `x`.

If you use a [custom plans directory](#custom-plan-directory-and-policies),
those files are not automatically deleted and must be managed manually.