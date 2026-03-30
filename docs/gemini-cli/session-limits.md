### Session limits

You can limit the length of individual sessions to prevent context windows from
becoming too large and expensive.

```json
{
  "model": {
    "maxSessionTurns": 100
  }
}
```

- **`maxSessionTurns`**: (number) The maximum number of turns (user and model
  exchanges) allowed in a single session. Set to `-1` for unlimited (default).

  **Behavior when limit is reached:**
  - **Interactive mode:** The CLI shows an informational message and stops
    sending requests to the model. You must manually start a new session.
  - **Non-interactive mode:** The CLI exits with an error.