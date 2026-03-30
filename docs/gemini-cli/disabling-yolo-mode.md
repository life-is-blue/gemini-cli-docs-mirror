### Disabling YOLO mode

To ensure that users cannot bypass the confirmation prompt for tool execution,
you can disable YOLO mode at the policy level. This adds a critical layer of
safety, as it prevents the model from executing tools without explicit user
approval.

**Example:** Force all tool executions to require user confirmation.

```json
{
  "security": {
    "disableYoloMode": true
  }
}
```

This setting is highly recommended in an enterprise environment to prevent
unintended tool execution.