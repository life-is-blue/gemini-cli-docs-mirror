### Metrics

Metrics provide numerical measurements of behavior over time.

#### Custom metrics

Gemini CLI exports several custom metrics.

##### Sessions

##### `gemini_cli.session.count`

Incremented once per CLI startup.

##### Onboarding

Tracks onboarding flow from authentication to the user

- `gemini_cli.onboarding.start` (Counter, Int): Incremented when the
  authentication flow begins.

- `gemini_cli.onboarding.success` (Counter, Int): Incremented when the user
onboarding flow completes successfully.
<details>
<summary>Attributes (Success)</summary>

- `user_tier` (string)

##### Tools

##### `gemini_cli.tool.call.count`

Counts tool calls.

<details>
<summary>Attributes</summary>

- `function_name` (string)
- `success` (boolean)
- `decision` (string: "accept", "reject", "modify", or "auto_accept")
- `tool_type` (string: "mcp" or "native")

</details>

##### `gemini_cli.tool.call.latency`

Measures tool call latency (in ms).

<details>
<summary>Attributes</summary>

- `function_name` (string)

</details>

##### API

##### `gemini_cli.api.request.count`

Counts all API requests.

<details>
<summary>Attributes</summary>

- `model` (string)
- `status_code` (int or string)
- `error_type` (string, optional)

</details>

##### `gemini_cli.api.request.latency`

Measures API request latency (in ms).

<details>
<summary>Attributes</summary>

- `model` (string)

</details>

##### Token usage

##### `gemini_cli.token.usage`

Counts input, output, thought, cache, and tool tokens.

<details>
<summary>Attributes</summary>

- `model` (string)
- `type` (string: "input", "output", "thought", "cache", or "tool")

</details>

##### Files

##### `gemini_cli.file.operation.count`

Counts file operations.

<details>
<summary>Attributes</summary>

- `operation` (string: "create", "read", or "update")
- `lines` (int, optional)
- `mimetype` (string, optional)
- `extension` (string, optional)
- `programming_language` (string, optional)

</details>

##### `gemini_cli.lines.changed`

Counts added or removed lines.

<details>
<summary>Attributes</summary>

- `function_name` (string, optional)
- `type` (string: "added" or "removed")

</details>

##### Chat and streaming

##### `gemini_cli.chat_compression`

Counts compression operations.

<details>
<summary>Attributes</summary>

- `tokens_before` (int)
- `tokens_after` (int)

</details>

##### `gemini_cli.chat.invalid_chunk.count`

Counts invalid stream chunks.

##### `gemini_cli.chat.content_retry.count`

Counts content error retries.

##### `gemini_cli.chat.content_retry_failure.count`

Counts requests where all retries failed.

##### Model routing

##### `gemini_cli.slash_command.model.call_count`

Counts model selections.

<details>
<summary>Attributes</summary>

- `slash_command.model.model_name` (string)

</details>

##### `gemini_cli.model_routing.latency`

Measures routing decision latency.

<details>
<summary>Attributes</summary>

- `routing.decision_model` (string)
- `routing.decision_source` (string)
- `routing.approval_mode` (string)

</details>

##### `gemini_cli.model_routing.failure.count`

Counts routing failures.

<details>
<summary>Attributes</summary>

- `routing.decision_source` (string)
- `routing.error_message` (string)
- `routing.approval_mode` (string)

</details>

##### Agent runs

##### `gemini_cli.agent.run.count`

Counts agent runs.

<details>
<summary>Attributes</summary>

- `agent_name` (string)
- `terminate_reason` (string)

</details>

##### `gemini_cli.agent.duration`

Measures agent run duration.

<details>
<summary>Attributes</summary>

- `agent_name` (string)

</details>

##### `gemini_cli.agent.turns`

Counts turns per agent run.

<details>
<summary>Attributes</summary>

- `agent_name` (string)

</details>

##### Approval mode

##### `gemini_cli.plan.execution.count`

Counts plan executions.

<details>
<summary>Attributes</summary>

- `approval_mode` (string)

</details>

##### UI

##### `gemini_cli.ui.flicker.count`

Counts terminal flicker events.

##### Performance

Gemini CLI provides detailed performance metrics for advanced monitoring.

##### `gemini_cli.startup.duration`

Measures startup time by phase.

<details>
<summary>Attributes</summary>

- `phase` (string)
- `details` (map, optional)

</details>

##### `gemini_cli.memory.usage`

Measures heap and RSS memory.

<details>
<summary>Attributes</summary>

- `memory_type` (string: "heap_used", "heap_total", "external", "rss")
- `component` (string, optional)

</details>

##### `gemini_cli.cpu.usage`

Measures CPU usage percentage.

<details>
<summary>Attributes</summary>

- `component` (string, optional)

</details>

##### `gemini_cli.tool.queue.depth`

Measures tool execution queue depth.

##### `gemini_cli.tool.execution.breakdown`

Breaks down tool time by phase.

<details>
<summary>Attributes</summary>

- `function_name` (string)
- `phase` (string: "validation", "preparation", "execution",
  "result_processing")

</details>

#### GenAI semantic convention

These metrics follow standard [OpenTelemetry GenAI semantic conventions].

- `gen_ai.client.token.usage`: Counts tokens used per operation.
- `gen_ai.client.operation.duration`: Measures operation duration in seconds.

[OpenTelemetry GenAI semantic conventions]:
  https://github.com/open-telemetry/semantic-conventions/blob/main/docs/gen-ai/gen-ai-metrics.md