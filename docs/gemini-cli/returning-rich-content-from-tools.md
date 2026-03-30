## Returning rich content from tools

MCP tools are not limited to returning simple text. You can return rich,
multi-part content, including text, images, audio, and other binary data in a
single tool response. This allows you to build powerful tools that can provide
diverse information to the model in a single turn.

All data returned from the tool is processed and sent to the model as context
for its next generation, enabling it to reason about or summarize the provided
information.