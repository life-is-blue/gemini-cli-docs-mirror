### Hook configuration

| Field         | Type     | Required  | Description                                                          |
| :------------ | :------- | :-------- | :------------------------------------------------------------------- |
| `type`        | `string` | **Yes**   | The execution engine. Currently only `"command"` is supported.       |
| `command`     | `string` | **Yes\*** | The shell command to execute. (Required when `type` is `"command"`). |
| `name`        | `string` | No        | A friendly name for identifying the hook in logs and CLI commands.   |
| `timeout`     | `number` | No        | Execution timeout in milliseconds (default: 60000).                  |
| `description` | `string` | No        | A brief explanation of the hook's purpose.                           |

---