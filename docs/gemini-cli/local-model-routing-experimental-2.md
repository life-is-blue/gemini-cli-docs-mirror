# [Local Model Routing (experimental)](http://geminicli.com/docs/core/local-model-routing.md)


Gemini CLI supports using a local model for
[routing decisions](/docs/cli/model-routing). When configured, Gemini CLI will
use a locally-running **Gemma** model to make routing decisions (instead of
sending routing decisions to a hosted model).

This feature can help reduce costs associated with hosted model usage while
offering similar routing decision latency and quality.

> **Note: Local model routing is currently an experimental feature.**