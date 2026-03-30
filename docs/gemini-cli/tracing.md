## Tracing

Gemini CLI uses OpenTelemetry (OTel) to record traces that help you debug agent
behavior. Traces instrument key events like model calls, tool scheduler
operations, and tool calls.

Traces provide deep visibility into agent behavior and help you debug complex
issues. They are captured automatically when you enable telemetry.