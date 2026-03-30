## Automatic Model Routing

When using an [auto model](/docs/reference/configuration#model), Gemini CLI
automatically optimizes [model routing](/docs/cli/telemetry#model-routing) based
on the current phase of your task:

1.  **Planning Phase:** While in Plan Mode, the CLI routes requests to a
    high-reasoning **Pro** model to ensure robust architectural decisions and
    high-quality plans.
2.  **Implementation Phase:** Once a plan is approved and you exit Plan Mode,
    the CLI detects the existence of the approved plan and automatically
    switches to a high-speed **Flash** model. This provides a faster, more
    responsive experience during the implementation of the plan.

This behavior is enabled by default to provide the best balance of quality and
performance. You can disable this automatic switching in your settings:

```json
{
  "general": {
    "plan": {
      "modelRouting": false
    }
  }
}
```