## Enable notifications

Notifications are disabled by default. You can enable them using the `/settings`
command or by updating your `settings.json` file.

1.  Open the settings dialog by typing `/settings` in an interactive session.
2.  Navigate to the **General** category.
3.  Toggle the **Enable Notifications** setting to **On**.

Alternatively, add the following to your `settings.json`:

```json
{
  "general": {
    "enableNotifications": true
  }
}
```