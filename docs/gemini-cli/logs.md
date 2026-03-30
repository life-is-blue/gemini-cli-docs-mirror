### Logs

Logs provide timestamped records of specific events. Gemini CLI logs events
across several categories.

#### Sessions

Session logs capture startup configuration and prompt submissions.

##### `gemini_cli.config`

Emitted at startup with the CLI configuration.

<details>
<summary>Attributes</summary>

- `model` (string)
- `embedding_model` (string)
- `sandbox_enabled` (boolean)
- `core_tools_enabled` (string)
- `approval_mode` (string)
- `api_key_enabled` (boolean)
- `vertex_ai_enabled` (boolean)
- `log_user_prompts_enabled` (boolean)
- `file_filtering_respect_git_ignore` (boolean)
- `debug_mode` (boolean)
- `mcp_servers` (string)
- `mcp_servers_count` (int)
- `mcp_tools` (string)
- `mcp_tools_count` (int)
- `output_format` (string)
- `extensions` (string)
- `extension_ids` (string)
- `extensions_count` (int)
- `auth_type` (string)
- `worktree_active` (boolean)
- `github_workflow_name` (string, optional)
- `github_repository_hash` (string, optional)
- `github_event_name` (string, optional)
- `github_pr_number` (string, optional)
- `github_issue_number` (string, optional)
- `github_custom_tracking_id` (string, optional)

</details>

##### `gemini_cli.user_prompt`

Emitted when you submit a prompt.

<details>
<summary>Attributes</summary>

- `prompt_length` (int)
- `prompt_id` (string)
- `prompt` (string; excluded if `telemetry.logPrompts` is `false`)
- `auth_type` (string)

</details>

#### Approval mode

These logs track changes to and usage of different approval modes.

##### Lifecycle

##### `approval_mode_switch`

Logs when you change the approval mode.

<details>
<summary>Attributes</summary>

- `from_mode` (string)
- `to_mode` (string)

</details>

##### `approval_mode_duration`

Records time spent in an approval mode.

<details>
<summary>Attributes</summary>

- `mode` (string)
- `duration_ms` (int)

</details>

##### Execution

##### `plan_execution`

Logs when you execute a plan and switch from plan mode to active execution.

<details>
<summary>Attributes</summary>

- `approval_mode` (string)

</details>

#### Tools

Tool logs capture executions, truncation, and edit behavior.

##### `gemini_cli.tool_call`

Emitted for each tool (function) call.

<details>
<summary>Attributes</summary>

- `function_name` (string)
- `function_args` (string)
- `duration_ms` (int)
- `success` (boolean)
- `decision` (string: "accept", "reject", "auto_accept", or "modify")
- `error` (string, optional)
- `error_type` (string, optional)
- `prompt_id` (string)
- `tool_type` (string: "native" or "mcp")
- `mcp_server_name` (string, optional)
- `extension_name` (string, optional)
- `extension_id` (string, optional)
- `content_length` (int, optional)
- `start_time` (number, optional)
- `end_time` (number, optional)
- `metadata` (object, optional), which may include:
  - `model_added_lines` (number)
  - `model_removed_lines` (number)
  - `user_added_lines` (number)
  - `user_removed_lines` (number)
  - `ask_user` (object)

</details>

##### `gemini_cli.tool_output_truncated`

Logs when tool output is truncated.

<details>
<summary>Attributes</summary>

- `tool_name` (string)
- `original_content_length` (int)
- `truncated_content_length` (int)
- `threshold` (int)
- `lines` (int)
- `prompt_id` (string)

</details>

##### `gemini_cli.edit_strategy`

Records the chosen edit strategy.

<details>
<summary>Attributes</summary>

- `strategy` (string)

</details>

##### `gemini_cli.edit_correction`

Records the result of an edit correction.

<details>
<summary>Attributes</summary>

- `correction` (string: "success" or "failure")

</details>

##### `gen_ai.client.inference.operation.details`

Provides detailed GenAI operation data aligned with OpenTelemetry conventions.

<details>
<summary>Attributes</summary>

- `gen_ai.request.model` (string)
- `gen_ai.provider.name` (string)
- `gen_ai.operation.name` (string)
- `gen_ai.input.messages` (json string)
- `gen_ai.output.messages` (json string)
- `gen_ai.response.finish_reasons` (array of strings)
- `gen_ai.usage.input_tokens` (int)
- `gen_ai.usage.output_tokens` (int)
- `gen_ai.request.temperature` (float)
- `gen_ai.request.top_p` (float)
- `gen_ai.request.top_k` (int)
- `gen_ai.request.max_tokens` (int)
- `gen_ai.system_instructions` (json string)
- `server.address` (string)
- `server.port` (int)

</details>

#### Files

File logs track operations performed by tools.

##### `gemini_cli.file_operation`

Emitted for each file creation, read, or update.

<details>
<summary>Attributes</summary>

- `tool_name` (string)
- `operation` (string: "create", "read", or "update")
- `lines` (int, optional)
- `mimetype` (string, optional)
- `extension` (string, optional)
- `programming_language` (string, optional)

</details>

#### API

API logs capture requests, responses, and errors from Gemini API.

##### `gemini_cli.api_request`

Request sent to Gemini API.

<details>
<summary>Attributes</summary>

- `model` (string)
- `prompt_id` (string)
- `role` (string: "user", "model", or "system")
- `request_text` (string, optional)

</details>

##### `gemini_cli.api_response`

Response received from Gemini API.

<details>
<summary>Attributes</summary>

- `model` (string)
- `status_code` (int or string)
- `duration_ms` (int)
- `input_token_count` (int)
- `output_token_count` (int)
- `cached_content_token_count` (int)
- `thoughts_token_count` (int)
- `tool_token_count` (int)
- `total_token_count` (int)
- `prompt_id` (string)
- `auth_type` (string)
- `finish_reasons` (array of strings)
- `response_text` (string, optional)

</details>

##### `gemini_cli.api_error`

Logs when an API request fails.

<details>
<summary>Attributes</summary>

- `error.message` (string)
- `model_name` (string)
- `duration` (int)
- `prompt_id` (string)
- `auth_type` (string)
- `error_type` (string, optional)
- `status_code` (int or string, optional)
- `role` (string, optional)

</details>

##### `gemini_cli.malformed_json_response`

Logs when a JSON response cannot be parsed.

<details>
<summary>Attributes</summary>

- `model` (string)

</details>

#### Model routing

These logs track how Gemini CLI selects and routes requests to models.

##### `gemini_cli.slash_command`

Logs slash command execution.

<details>
<summary>Attributes</summary>

- `command` (string)
- `subcommand` (string, optional)
- `status` (string: "success" or "error")

</details>

##### `gemini_cli.slash_command.model`

Logs model selection via slash command.

<details>
<summary>Attributes</summary>

- `model_name` (string)

</details>

##### `gemini_cli.model_routing`

Records model router decisions and reasoning.

<details>
<summary>Attributes</summary>

- `decision_model` (string)
- `decision_source` (string)
- `routing_latency_ms` (int)
- `reasoning` (string, optional)
- `failed` (boolean)
- `error_message` (string, optional)
- `approval_mode` (string)

</details>

#### Chat and streaming

These logs track chat context compression and streaming chunk errors.

##### `gemini_cli.chat_compression`

Logs chat context compression events.

<details>
<summary>Attributes</summary>

- `tokens_before` (int)
- `tokens_after` (int)

</details>

##### `gemini_cli.chat.invalid_chunk`

Logs invalid chunks received in a stream.

<details>
<summary>Attributes</summary>

- `error_message` (string, optional)

</details>

##### `gemini_cli.chat.content_retry`

Logs retries due to content errors.

<details>
<summary>Attributes</summary>

- `attempt_number` (int)
- `error_type` (string)
- `retry_delay_ms` (int)
- `model` (string)

</details>

##### `gemini_cli.chat.content_retry_failure`

Logs when all content retries fail.

<details>
<summary>Attributes</summary>

- `total_attempts` (int)
- `final_error_type` (string)
- `total_duration_ms` (int, optional)
- `model` (string)

</details>

##### `gemini_cli.conversation_finished`

Logs when a conversation session ends.

<details>
<summary>Attributes</summary>

- `approvalMode` (string)
- `turnCount` (int)

</details>

#### Resilience

Resilience logs record fallback mechanisms and recovery attempts.

##### `gemini_cli.flash_fallback`

Logs switch to a flash model fallback.

<details>
<summary>Attributes</summary>

- `auth_type` (string)

</details>

##### `gemini_cli.ripgrep_fallback`

Logs fallback to standard grep.

<details>
<summary>Attributes</summary>

- `error` (string, optional)

</details>

##### `gemini_cli.web_fetch_fallback_attempt`

Logs web-fetch fallback attempts.

<details>
<summary>Attributes</summary>

- `reason` (string: "private_ip" or "primary_failed")

</details>

##### `gemini_cli.agent.recovery_attempt`

Logs attempts to recover from agent errors.

<details>
<summary>Attributes</summary>

- `agent_name` (string)
- `attempt_number` (int)
- `success` (boolean)
- `error_type` (string, optional)

</details>

#### Extensions

Extension logs track lifecycle events and settings changes.

##### `gemini_cli.extension_install`

Logs when you install an extension.

<details>
<summary>Attributes</summary>

- `extension_name` (string)
- `extension_version` (string)
- `extension_source` (string)
- `status` (string)

</details>

##### `gemini_cli.extension_uninstall`

Logs when you uninstall an extension.

<details>
<summary>Attributes</summary>

- `extension_name` (string)
- `status` (string)

</details>

##### `gemini_cli.extension_enable`

Logs when you enable an extension.

<details>
<summary>Attributes</summary>

- `extension_name` (string)
- `setting_scope` (string)

</details>

##### `gemini_cli.extension_disable`

Logs when you disable an extension.

<details>
<summary>Attributes</summary>

- `extension_name` (string)
- `setting_scope` (string)

</details>

#### Agent runs

Agent logs track the lifecycle of agent executions.

##### `gemini_cli.agent.start`

Logs when an agent run begins.

<details>
<summary>Attributes</summary>

- `agent_id` (string)
- `agent_name` (string)

</details>

##### `gemini_cli.agent.finish`

Logs when an agent run completes.

<details>
<summary>Attributes</summary>

- `agent_id` (string)
- `agent_name` (string)
- `duration_ms` (int)
- `turn_count` (int)
- `terminate_reason` (string)

</details>

#### IDE

IDE logs capture connectivity events for the IDE companion.

##### `gemini_cli.ide_connection`

Logs IDE companion connections.

<details>
<summary>Attributes</summary>

- `connection_type` (string)

</details>

#### UI

UI logs track terminal rendering issues.

##### `kitty_sequence_overflow`

Logs terminal control sequence overflows.

<details>
<summary>Attributes</summary>

- `sequence_length` (int)
- `truncated_sequence` (string)

</details>

#### Miscellaneous

##### `gemini_cli.rewind`

Logs when the conversation state is rewound.

<details>
<summary>Attributes</summary>

- `outcome` (string)

</details>

##### `gemini_cli.conseca.verdict`

Logs security verdicts from ConSeca.

<details>
<summary>Attributes</summary>

- `verdict` (string)
- `decision` (string: "accept", "reject", or "modify")
- `reason` (string, optional)
- `tool_name` (string, optional)

</details>

##### `gemini_cli.hook_call`

Logs execution of lifecycle hooks.

<details>
<summary>Attributes</summary>

- `hook_name` (string)
- `hook_type` (string)
- `duration_ms` (int)
- `success` (boolean)

</details>

##### `gemini_cli.tool_output_masking`

Logs when tool output is masked for privacy.

<details>
<summary>Attributes</summary>

- `tokens_before` (int)
- `tokens_after` (int)
- `masked_count` (int)
- `total_prunable_tokens` (int)

</details>

##### `gemini_cli.keychain.availability`

Logs keychain availability checks.

<details>
<summary>Attributes</summary>

- `available` (boolean)

##### `gemini_cli.startup_stats`

Logs detailed startup performance statistics.

<details>
<summary>Attributes</summary>

- `phases` (json array of startup phases)
- `os_platform` (string)
- `os_release` (string)
- `is_docker` (boolean)

</details>

</details>