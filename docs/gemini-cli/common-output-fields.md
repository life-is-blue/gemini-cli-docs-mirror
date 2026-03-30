## Common output fields

Most hooks support these fields in their `stdout` JSON:

| Field            | Type      | Description                                                                    |
| :--------------- | :-------- | :----------------------------------------------------------------------------- |
| `systemMessage`  | `string`  | Displayed immediately to the user in the terminal.                             |
| `suppressOutput` | `boolean` | If `true`, hides internal hook metadata from logs/telemetry.                   |
| `continue`       | `boolean` | If `false`, stops the entire agent loop immediately.                           |
| `stopReason`     | `string`  | Displayed to the user when `continue` is `false`.                              |
| `decision`       | `string`  | `"allow"` or `"deny"` (alias `"block"`). Specific impact depends on the event. |
| `reason`         | `string`  | The feedback/error message provided when a `decision` is `"deny"`.             |

---