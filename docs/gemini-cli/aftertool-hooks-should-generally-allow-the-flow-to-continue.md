# AfterTool hooks should generally allow the flow to continue
echo '{"decision": "allow"}'
```

To register this `AfterTool` hook, add it to your `settings.json`:

```json
{
  "hooks": {
    "AfterTool": [
      {
        "matcher": "exit_plan_mode",
        "hooks": [
          {
            "name": "archive-plan",
            "type": "command",
            "command": "./.gemini/hooks/archive-plan.sh"
          }
        ]
      }
    ]
  }
}
```