## Base input schema

All hooks receive these common fields via `stdin`:

```typescript
{
  "session_id": string,      // Unique ID for the current session
  "transcript_path": string, // Absolute path to session transcript JSON
  "cwd": string,             // Current working directory
  "hook_event_name": string, // The firing event (e.g. "BeforeTool")
  "timestamp": string        // ISO 8601 execution time
}
```

---