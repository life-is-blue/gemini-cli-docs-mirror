### Local Model Routing (Experimental)

Gemini CLI supports using a local model for routing decisions. When configured,
Gemini CLI will use a locally-running **Gemma** model to make routing decisions
(instead of sending routing decisions to a hosted model). This feature can help
reduce costs associated with hosted model usage while offering similar routing
decision latency and quality.

In order to use this feature, the local Gemma model **must** be served behind a
Gemini API and accessible via HTTP at an endpoint configured in `settings.json`.

For more details on how to configure local model routing, see
[Local Model Routing](/docs/core/local-model-routing).