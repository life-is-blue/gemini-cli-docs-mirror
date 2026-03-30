### `PreCompress`

Fires before the CLI summarizes history to save tokens. Used for logging or
state saving.

- **Input Fields**:
  - `trigger`: (`"auto" | "manual"`)
- **Relevant Output Fields**:
  - `systemMessage`: Displayed to the user before compression.
- **Advisory Only**: Fired asynchronously. It **cannot** block or modify the
  compression process. Flow-control fields are ignored.

---