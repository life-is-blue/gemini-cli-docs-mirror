### `GenerateContentConfig` (Common Parameters)

Directly maps to the SDK's `GenerateContentConfig`. Common parameters include:

- **`temperature`**: (`number`) Controls output randomness. Lower values (0.0)
  are deterministic; higher values (>0.7) are creative.
- **`topP`**: (`number`) Nucleus sampling probability.
- **`maxOutputTokens`**: (`number`) Limit on generated response length.
- **`thinkingConfig`**: (`object`) Configuration for models with reasoning
  capabilities (e.g., `thinkingBudget`, `includeThoughts`).