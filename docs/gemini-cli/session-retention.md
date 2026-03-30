### Session retention

By default, Gemini CLI automatically cleans up old session data to prevent your
history from growing indefinitely. When a session is deleted, Gemini CLI also
removes all associated data, including implementation plans, task trackers, tool
outputs, and activity logs.

The default policy is to **retain sessions for 30 days**.

#### Configuration

You can customize these policies using the `/settings` command or by manually
editing your `settings.json` file:

```json
{
  "general": {
    "sessionRetention": {
      "enabled": true,
      "maxAge": "30d",
      "maxCount": 50
    }
  }
}
```

- **`enabled`**: (boolean) Master switch for session cleanup. Defaults to
  `true`.
- **`maxAge`**: (string) Duration to keep sessions (for example, "24h", "7d",
  "4w"). Sessions older than this are deleted. Defaults to `"30d"`.
- **`maxCount`**: (number) Maximum number of sessions to retain. The oldest
  sessions exceeding this count are deleted. Defaults to undefined (unlimited).
- **`minRetention`**: (string) Minimum retention period (safety limit). Defaults
  to `"1d"`. Sessions newer than this period are never deleted by automatic
  cleanup.