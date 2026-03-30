### Traces

Traces provide an "under-the-hood" view of agent and backend operations. Use
traces to debug tool interactions and optimize performance.

Every trace captures rich metadata via standard span attributes.

<details open>
<summary>Standard span attributes</summary>

- `gen_ai.operation.name`: High-level operation (for example, `tool_call`,
  `llm_call`, `user_prompt`, `system_prompt`, `agent_call`, or
  `schedule_tool_calls`).
- `gen_ai.agent.name`: Set to `gemini-cli`.
- `gen_ai.agent.description`: The service agent description.
- `gen_ai.input.messages`: Input data or metadata.
- `gen_ai.output.messages`: Output data or results.
- `gen_ai.request.model`: Request model name.
- `gen_ai.response.model`: Response model name.
- `gen_ai.prompt.name`: The prompt name.
- `gen_ai.tool.name`: Executed tool name.
- `gen_ai.tool.call_id`: Unique ID for the tool call.
- `gen_ai.tool.description`: Tool description.
- `gen_ai.tool.definitions`: Tool definitions in JSON format.
- `gen_ai.usage.input_tokens`: Number of input tokens.
- `gen_ai.usage.output_tokens`: Number of output tokens.
- `gen_ai.system_instructions`: System instructions in JSON format.
- `gen_ai.conversation.id`: The CLI session ID.

</details>

For more details on semantic conventions for events, see the
[OpenTelemetry documentation](https://github.com/open-telemetry/semantic-conventions/blob/8b4f210f43136e57c1f6f47292eb6d38e3bf30bb/docs/gen-ai/gen-ai-events.md).