### Inline Agent Card JSON

<details>
<summary>View formatting options for JSON strings</summary>

If you don't have an endpoint serving the agent card, you can provide the A2A
card directly as a JSON string using `agent_card_json`.

When providing a JSON string in YAML, you must properly format it as a string
scalar. You can use single quotes, a block scalar, or double quotes (which
require escaping internal double quotes).

#### Using single quotes

Single quotes allow you to embed unescaped double quotes inside the JSON string.
This format is useful for shorter, single-line JSON strings.

```markdown
---
kind: remote
name: single-quotes-agent
agent_card_json:
  '{ "protocolVersion": "0.3.0", "name": "Example Agent", "version": "1.0.0",
  "url": "dummy-url" }'
---
```

#### Using a block scalar

The literal block scalar (`|`) preserves line breaks and is highly recommended
for multiline JSON strings as it avoids quote escaping entirely. The following
is a complete, valid Agent Card configuration using dummy values.

```markdown
---
kind: remote
name: block-scalar-agent
agent_card_json: |
  {
    "protocolVersion": "0.3.0",
    "name": "Example Agent Name",
    "description": "An example agent description for documentation purposes.",
    "version": "1.0.0",
    "url": "dummy-url",
    "preferredTransport": "HTTP+JSON",
    "capabilities": {
      "streaming": true,
      "extendedAgentCard": false
    },
    "defaultInputModes": [
      "text/plain"
    ],
    "defaultOutputModes": [
      "application/json"
    ],
    "skills": [
      {
        "id": "ExampleSkill",
        "name": "Example Skill Assistant",
        "description": "A description of what this example skill does.",
        "tags": [
          "example-tag"
        ],
        "examples": [
          "Show me an example."
        ]
      }
    ]
  }
---
```

#### Using double quotes

Double quotes are also supported, but any internal double quotes in your JSON
must be escaped with a backslash.

```markdown
---
kind: remote
name: double-quotes-agent
agent_card_json:
  '{ "protocolVersion": "0.3.0", "name": "Example Agent", "version": "1.0.0",
  "url": "dummy-url" }'
---
```

</details>