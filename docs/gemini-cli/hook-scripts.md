### Hook Scripts

> **Note**: For brevity, these scripts use `console.error` for logging and
> standard `console.log` for JSON output.

#### 1. Initialize (`init.js`)

```javascript
#!/usr/bin/env node
// Initialize DB or resources
console.error('Initializing assistant...');

// Output to user
console.log(
  JSON.stringify({
    systemMessage: '🧠 Smart Assistant Loaded',
  }),
);
```

#### 2. Inject Memories (`inject-memories.js`)

```javascript
#!/usr/bin/env node
const fs = require('fs');

async function main() {
  const input = JSON.parse(fs.readFileSync(0, 'utf-8'));
  // Assume we fetch memories from a DB here
  const memories = '- [Memory] Always use TypeScript for this project.';

  console.log(
    JSON.stringify({
      hookSpecificOutput: {
        hookEventName: 'BeforeAgent',
        additionalContext: `\n## Relevant Memories\n${memories}`,
      },
    }),
  );
}
main();
```

#### 3. Security Check (`security.js`)

```javascript
#!/usr/bin/env node
const fs = require('fs');
const input = JSON.parse(fs.readFileSync(0));
const content = input.tool_input.content || '';

if (content.includes('SECRET_KEY')) {
  console.log(
    JSON.stringify({
      decision: 'deny',
      reason: 'Found SECRET_KEY in content',
      systemMessage: '🚨 Blocked sensitive commit',
    }),
  );
  process.exit(0);
}

console.log(JSON.stringify({ decision: 'allow' }));
```

#### 4. Record Interaction (`record.js`)

```javascript
#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const input = JSON.parse(fs.readFileSync(0));
const { llm_request, llm_response } = input;
const logFile = path.join(
  process.env.GEMINI_PROJECT_DIR,
  '.gemini/memory/session.jsonl',
);

fs.appendFileSync(
  logFile,
  JSON.stringify({
    request: llm_request,
    response: llm_response,
    timestamp: new Date().toISOString(),
  }) + '\n',
);

console.log(JSON.stringify({}));
```

#### 5. Validate Response (`validate.js`)

```javascript
#!/usr/bin/env node
const fs = require('fs');
const input = JSON.parse(fs.readFileSync(0));
const response = input.prompt_response;

// Example: Check if the agent forgot to include a summary
if (!response.includes('Summary:')) {
  console.log(
    JSON.stringify({
      decision: 'block', // Triggers an automatic retry turn
      reason: 'Your response is missing a Summary section. Please add one.',
      systemMessage: '🔄 Requesting missing summary...',
    }),
  );
  process.exit(0);
}

console.log(JSON.stringify({ decision: 'allow' }));
```

#### 6. Consolidate Memories (`consolidate.js`)

```javascript
#!/usr/bin/env node
// Logic to save final session state
console.error('Consolidating memories for session end...');
```