## Model fallback

Gemini CLI includes a model fallback mechanism to ensure that you can continue
to use the CLI even if the default "pro" model is rate-limited.

If you are using the default "pro" model and the CLI detects that you are being
rate-limited, it automatically switches to the "flash" model for the current
session. This allows you to continue working without interruption.

Internal utility calls that use `gemini-2.5-flash-lite` (for example, prompt
completion and classification) silently fall back to `gemini-2.5-flash` and
`gemini-2.5-pro` when quota is exhausted, without changing the configured model.