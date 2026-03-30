### RAG-based Tool Filtering (BeforeToolSelection)

Use `BeforeToolSelection` to intelligently reduce the tool space. This example
uses a Node.js script to check the user's prompt and allow only relevant tools.

**`.gemini/hooks/filter-tools.js`:**

```javascript
#!/usr/bin/env node
const fs = require('fs');

async function main() {
  const input = JSON.parse(fs.readFileSync(0, 'utf-8'));
  const { llm_request } = input;

  // Decoupled API: Access messages from llm_request
  const messages = llm_request.messages || [];
  const lastUserMessage = messages
    .slice()
    .reverse()
    .find((m) => m.role === 'user');

  if (!lastUserMessage) {
    console.log(JSON.stringify({})); // Do nothing
    return;
  }

  const text = lastUserMessage.content;
  const allowed = ['write_todos']; // Always allow memory

  // Simple keyword matching
  if (text.includes('read') || text.includes('check')) {
    allowed.push('read_file', 'list_directory');
  }
  if (text.includes('test')) {
    allowed.push('run_shell_command');
  }

  // If we found specific intent, filter tools. Otherwise allow all.
  if (allowed.length > 1) {
    console.log(
      JSON.stringify({
        hookSpecificOutput: {
          hookEventName: 'BeforeToolSelection',
          toolConfig: {
            mode: 'ANY', // Force usage of one of these tools (or AUTO)
            allowedFunctionNames: allowed,
          },
        },
      }),
    );
  } else {
    console.log(JSON.stringify({}));
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
```

**`.gemini/settings.json`:**

```json
{
  "hooks": {
    "BeforeToolSelection": [
      {
        "matcher": "*",
        "hooks": [
          {
            "name": "intent-filter",
            "type": "command",
            "command": "node .gemini/hooks/filter-tools.js"
          }
        ]
      }
    ]
  }
}
```

> **TIP**
>
> **Union Aggregation Strategy**: `BeforeToolSelection` is unique in that it
> combines the results of all matching hooks. If you have multiple filtering
> hooks, the agent will receive the **union** of all whitelisted tools. Only
> using `mode: "NONE"` will override other hooks to disable all tools.