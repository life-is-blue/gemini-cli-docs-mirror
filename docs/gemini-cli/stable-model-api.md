## Stable Model API

Gemini CLI uses these structures to ensure hooks don't break across SDK updates.

**LLMRequest**:

```typescript
{
  "model": string,
  "messages": Array<{
    "role": "user" | "model" | "system",
    "content": string // Non-text parts are filtered out for hooks
  }>,
  "config": { "temperature": number, ... },
  "toolConfig": { "mode": string, "allowedFunctionNames": string[] }
}

```

**LLMResponse**:

```typescript
{
  "candidates": Array<{
    "content": { "role": "model", "parts": string[] },
    "finishReason": string
  }>,
  "usageMetadata": { "totalTokenCount": number }
}
```