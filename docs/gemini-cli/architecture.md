### Architecture

1. **SessionStart**: Load project memories.
2. **BeforeAgent**: Inject memories into context.
3. **BeforeToolSelection**: Filter tools based on intent.
4. **BeforeTool**: Scan for secrets.
5. **AfterModel**: Record interactions.
6. **AfterAgent**: Validate final response quality (Retry).
7. **SessionEnd**: Consolidate memories.