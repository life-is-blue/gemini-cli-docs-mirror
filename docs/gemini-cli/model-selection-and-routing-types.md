### Model selection and routing types

When using Gemini CLI, you may want to control how your requests are routed
between models. By default, Gemini CLI uses **Auto** routing.

When using Gemini 3 Pro, you may want to use Auto routing or Pro routing to
manage your usage limits:

- **Auto routing:** Auto routing first determines whether a prompt involves a
  complex or simple operation. For simple prompts, it will automatically use
  Gemini 2.5 Flash. For complex prompts, if Gemini 3 Pro is enabled, it will use
  Gemini 3 Pro; otherwise, it will use Gemini 2.5 Pro.
- **Pro routing:** If you want to ensure your task is processed by the most
  capable model, use `/model` and select **Pro**. Gemini CLI will prioritize the
  most capable model available, including Gemini 3 Pro if it has been enabled.

To learn more about selecting a model and routing, refer to
[Gemini CLI Model Selection](/docs/cli/model).