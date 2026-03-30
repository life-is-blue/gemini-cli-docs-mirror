### Use appropriate events

Choose hook events that match your use case to avoid unnecessary execution.

- **`AfterAgent`**: Fires **once** per turn after the model finishes its final
  response. Use this for quality validation (Retries) or final logging.
- **`AfterModel`**: Fires after **every chunk** of LLM output. Use this for
  real-time redaction, PII filtering, or monitoring output as it streams.

If you only need to check the final completion, use `AfterAgent` to save
performance.