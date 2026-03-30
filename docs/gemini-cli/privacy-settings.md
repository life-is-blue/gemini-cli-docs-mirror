### Privacy settings

**Disable PII logging:** If you are working with sensitive data, disable prompt
logging in your settings:

```json
{
  "telemetry": {
    "logPrompts": false
  }
}
```

**Suppress Output:** Individual hooks can request their metadata be hidden from
logs and telemetry by returning `"suppressOutput": true` in their JSON response.

> **Note**

> `suppressOutput` only affects background logging. Any `systemMessage` or
> `reason` included in the JSON will still be displayed to the user in the
> terminal.