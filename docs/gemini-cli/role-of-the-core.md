## Role of the core

While the `packages/cli` portion of Gemini CLI provides the user interface,
`packages/core` is responsible for:

- **Gemini API interaction:** Securely communicating with the Google Gemini API,
  sending user prompts, and receiving model responses.
- **Prompt engineering:** Constructing effective prompts for the Gemini model,
  potentially incorporating conversation history, tool definitions, and
  instructional context from `GEMINI.md` files.
- **Tool management & orchestration:**
  - Registering available tools (e.g., file system tools, shell command
    execution).
  - Interpreting tool use requests from the Gemini model.
  - Executing the requested tools with the provided arguments.
  - Returning tool execution results to the Gemini model for further processing.
- **Session and state management:** Keeping track of the conversation state,
  including history and any relevant context required for coherent interactions.
- **Configuration:** Managing core-specific configurations, such as API key
  access, model selection, and tool settings.