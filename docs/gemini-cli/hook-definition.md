### Hook definition

| Field        | Type      | Required | Description                                                                             |
| :----------- | :-------- | :------- | :-------------------------------------------------------------------------------------- |
| `matcher`    | `string`  | No       | A regex (for tools) or exact string (for lifecycle) to filter when the hook runs.       |
| `sequential` | `boolean` | No       | If `true`, hooks in this group run one after another. If `false`, they run in parallel. |
| `hooks`      | `array`   | **Yes**  | An array of **hook configurations**.                                                    |