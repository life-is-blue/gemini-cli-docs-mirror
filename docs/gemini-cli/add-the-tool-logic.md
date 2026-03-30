### Add the tool logic

Skills can bundle resources like scripts.

1.  Create a file at `.gemini/skills/api-auditor/scripts/audit.js`. This is the
    code the agent will run.

    ```javascript
    // .gemini/skills/api-auditor/scripts/audit.js
    const url = process.argv[2];

    if (!url) {
      console.error('Usage: node audit.js <url>');
      process.exit(1);
    }

    console.log(`Auditing ${url}...`);
    fetch(url, { method: 'HEAD' })
      .then((r) => console.log(`Result: Success (Status ${r.status})`))
      .catch((e) => console.error(`Result: Failed (${e.message})`));
    ```