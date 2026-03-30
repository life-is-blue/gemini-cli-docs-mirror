## Enabling the feature

The Trusted Folders feature is **disabled by default**. To use it, you must
first enable it in your settings.

Add the following to your user `settings.json` file:

```json
{
  "security": {
    "folderTrust": {
      "enabled": true
    }
  }
}
```