## How to enable Git worktrees

Git worktrees are an experimental feature. You must enable them in your settings
using the `/settings` command or by manually editing your `settings.json` file.

1.  Use the `/settings` command.
2.  Search for and set **Enable Git Worktrees** to `true`.

Alternatively, add the following to your `settings.json`:

```json
{
  "experimental": {
    "worktrees": true
  }
}
```