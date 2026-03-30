# This command will be invoked via: /refactor:pure

description = "Asks the model to refactor the current context into a pure function."

prompt = """
Please analyze the code I've provided in the current context.
Refactor it into a pure function.

Your response should include:
1. The refactored, pure function code block.
2. A brief explanation of the key changes you made and why they contribute to purity.
"""
```

**3. Run the command:**

That's it! You can now run your command in the CLI. First, you might add a file
to the context, and then invoke your command:

```
> @my-messy-function.js
> /refactor:pure
```

Gemini CLI will then execute the multi-line prompt defined in your TOML file.