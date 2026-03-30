### Documenting your hooks

Maintainability is critical for complex hook systems. Use descriptions and
comments to help yourself and others understand why a hook exists.

**Use the `description` field**: This text is displayed in the `/hooks panel` UI
and helps diagnose issues.

```json
{
  "hooks": {
    "BeforeTool": [
      {
        "matcher": "write_file|replace",
        "hooks": [
          {
            "name": "secret-scanner",
            "type": "command",
            "command": "$GEMINI_PROJECT_DIR/.gemini/hooks/block-secrets.sh",
            "description": "Scans code changes for API keys and secrets before writing"
          }
        ]
      }
    ]
  }
}
```

**Add comments in hook scripts**: Explain performance expectations and
dependencies.

```javascript
#!/usr/bin/env node
/**
 * RAG Tool Filter Hook
 *
 * Reduces the tool space by extracting keywords from the user's request.
 *
 * Performance: ~500ms average
 * Dependencies: @google/generative-ai
 */
```