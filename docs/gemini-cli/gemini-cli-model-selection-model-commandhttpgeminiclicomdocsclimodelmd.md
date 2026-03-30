# [Gemini CLI model selection (`/model` command)](http://geminicli.com/docs/cli/model.md)


Select your Gemini CLI model. The `/model` command lets you configure the model
used by Gemini CLI, giving you more control over your results. Use **Pro**
models for complex tasks and reasoning, **Flash** models for high speed results,
or the (recommended) **Auto** setting to choose the best model for your tasks.

<!-- prettier-ignore -->
> [!NOTE]
> The `/model` command (and the `--model` flag) does not override the
> model used by sub-agents. Consequently, even when using the `/model` flag you
> may see other models used in your model usage reports.