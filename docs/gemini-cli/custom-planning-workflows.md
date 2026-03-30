### Custom planning workflows

You can install or create specialized planners to suit your workflow.

#### Conductor

[Conductor] is designed for spec-driven development. It organizes work into
"tracks" and stores persistent artifacts in your project's `conductor/`
directory:

- **Automate transitions:** Switches to read-only mode via
  [`enter_plan_mode`](/docs/tools/planning#1-enter_plan_mode-enterplanmode).
- **Streamline decisions:** Uses [`ask_user`](/docs/tools/ask-user) for
  architectural choices.
- **Maintain project context:** Stores artifacts in the project directory using
  [custom plan directory and policies](#custom-plan-directory-and-policies).
- **Handoff execution:** Transitions to implementation via
  [`exit_plan_mode`](/docs/tools/planning#2-exit_plan_mode-exitplanmode).

#### Build your own

Since Plan Mode is built on modular building blocks, you can develop your own
custom planning workflow as an [extensions](/docs/extensions). By
leveraging core tools and [custom policies](#custom-policies), you can define
how Gemini CLI researches and stores plans for your specific domain.

To build a custom planning workflow, you can use:

- **Tool usage:** Use core tools like
  [`enter_plan_mode`](/docs/tools/planning#1-enter_plan_mode-enterplanmode),
  [`ask_user`](/docs/tools/ask-user), and
  [`exit_plan_mode`](/docs/tools/planning#2-exit_plan_mode-exitplanmode) to
  manage the research and design process.
- **Customization:** Set your own storage locations and policy rules using
  [custom plan directories](#custom-plan-directory-and-policies) and
  [custom policies](#custom-policies).

<!-- prettier-ignore -->
> [!TIP]
> Use [Conductor] as a reference when building your own custom
> planning workflow.

By using Plan Mode as its execution environment, your custom methodology can
enforce read-only safety during the design phase while benefiting from
high-reasoning model routing.