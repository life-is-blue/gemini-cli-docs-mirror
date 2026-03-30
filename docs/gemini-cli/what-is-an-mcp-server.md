## What is an MCP server?

An MCP server is an application that exposes tools and resources to the Gemini
CLI through the Model Context Protocol, allowing it to interact with external
systems and data sources. MCP servers act as a bridge between the Gemini model
and your local environment or other services like APIs.

An MCP server enables the Gemini CLI to:

- **Discover tools:** List available tools, their descriptions, and parameters
  through standardized schema definitions.
- **Execute tools:** Call specific tools with defined arguments and receive
  structured responses.
- **Access resources:** Read data from specific resources that the server
  exposes (files, API payloads, reports, etc.).

With an MCP server, you can extend the Gemini CLI's capabilities to perform
actions beyond its built-in features, such as interacting with databases, APIs,
custom scripts, or specialized workflows.