## Step 1: Create a new extension

The easiest way to start is by using a built-in template. We'll use the
`mcp-server` example as our foundation.

Run the following command to create a new directory called `my-first-extension`
with the template files:

```bash
gemini extensions new my-first-extension mcp-server
```

This creates a directory with the following structure:

```
my-first-extension/
├── example.js
├── gemini-extension.json
└── package.json
```