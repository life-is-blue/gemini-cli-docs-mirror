## How it works

Model routing is managed by the `ModelAvailabilityService`, which monitors model
health and automatically routes requests to available models based on defined
policies.

1.  **Model failure:** If the currently selected model fails (e.g., due to quota
    or server errors), the CLI will initiate the fallback process.

2.  **User consent:** Depending on the failure and the model's policy, the CLI
    may prompt you to switch to a fallback model (by default always prompts
    you).

    Some internal utility calls (such as prompt completion and classification)
    use a silent fallback chain for `gemini-2.5-flash-lite` and will fall back
    to `gemini-2.5-flash` and `gemini-2.5-pro` without prompting or changing the
    configured model.

3.  **Model switch:** If approved, or if the policy allows for silent fallback,
    the CLI will use an available fallback model for the current turn or the
    remainder of the session.