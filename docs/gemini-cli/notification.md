### `Notification`

Fires when the CLI emits a system alert (e.g., Tool Permissions). Used for
external logging or cross-platform alerts.

- **Input Fields**:
  - `notification_type`: (`"ToolPermission"`)
  - `message`: Summary of the alert.
  - `details`: JSON object with alert-specific metadata (e.g., tool name, file
    path).
- **Relevant Output Fields**:
  - `systemMessage`: Displayed alongside the system alert.
- **Observability Only**: This hook **cannot** block alerts or grant permissions
  automatically. Flow-control fields are ignored.