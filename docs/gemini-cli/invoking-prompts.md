### Invoking prompts

Once a prompt is discovered, you can invoke it using its name as a slash
command. The CLI will automatically handle parsing arguments.

```bash
/poem-writer --title="Gemini CLI" --mood="reverent"
```

or, using positional arguments:

```bash
/poem-writer "Gemini CLI" reverent
```

When you run this command, the Gemini CLI executes the `prompts/get` method on
the MCP server with the provided arguments. The server is responsible for
substituting the arguments into the prompt template and returning the final
prompt text. The CLI then sends this prompt to the model for execution. This
provides a convenient way to automate and share common workflows.