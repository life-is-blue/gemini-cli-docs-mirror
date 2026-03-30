### <a id="policy-engine"></a>Policy Engine

Extensions can contribute policy rules and safety checkers to the Gemini CLI
[Policy Engine](/docs/reference/policy-engine). These rules are defined in
`.toml` files and take effect when the extension is activated.

To add policies, create a `policies/` directory in your extension's root and
place your `.toml` policy files inside it. Gemini CLI automatically loads all
`.toml` files from this directory.

Rules contributed by extensions run in their own tier (tier 2), alongside
workspace-defined policies. This tier has higher priority than the default rules
but lower priority than user or admin policies.

<!-- prettier-ignore -->
> [!WARNING]
> For security, Gemini CLI ignores any `allow` decisions or `yolo`
> mode configurations in extension policies. This ensures that an extension
> cannot automatically approve tool calls or bypass security measures without
> your confirmation.

**Example `policies.toml`**

```toml
[[rule]]
mcpName = "my_server"
toolName = "dangerous_tool"
decision = "ask_user"
priority = 100

[[safety_checker]]
mcpName = "my_server"
toolName = "write_data"
priority = 200
[safety_checker.checker]
type = "in-process"
name = "allowed-path"
required_context = ["environment"]
```