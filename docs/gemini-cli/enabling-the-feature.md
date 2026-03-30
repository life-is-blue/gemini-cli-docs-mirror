## Enabling the feature

The Checkpointing feature is disabled by default. To enable it, you need to edit
your `settings.json` file.

<!-- prettier-ignore -->
> [!CAUTION]
> The `--checkpointing` command-line flag was removed in version
> 0.11.0. Checkpointing can now only be enabled through the `settings.json`
> configuration file.

Add the following key to your `settings.json`:

```json
{
  "general": {
    "checkpointing": {
      "enabled": true
    }
  }
}
```