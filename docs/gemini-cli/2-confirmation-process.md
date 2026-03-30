### 2. Confirmation process

Each `DiscoveredMCPTool` implements sophisticated confirmation logic:

#### Trust-based bypass

```typescript
if (this.trust) {
  return false; // No confirmation needed
}
```

#### Dynamic allow-listing

The system maintains internal allow-lists for:

- **Server-level:** `serverName` → All tools from this server are trusted
- **Tool-level:** `serverName.toolName` → This specific tool is trusted

#### User choice handling

When confirmation is required, users can choose:

- **Proceed once:** Execute this time only
- **Always allow this tool:** Add to tool-level allow-list
- **Always allow this server:** Add to server-level allow-list
- **Cancel:** Abort execution