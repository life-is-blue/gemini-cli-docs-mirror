### 5. Connection management

After discovery:

- **Persistent connections:** Servers that successfully register tools maintain
  their connections
- **Cleanup:** Servers that provide no usable tools have their connections
  closed
- **Status updates:** Final server statuses are set to `CONNECTED` or
  `DISCONNECTED`