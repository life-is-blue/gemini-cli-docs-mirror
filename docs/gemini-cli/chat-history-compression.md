## Chat history compression

To ensure that long conversations don't exceed the token limits of the Gemini
model, the core includes a chat history compression feature.

When a conversation approaches the token limit for the configured model, the
core automatically compresses the conversation history before sending it to the
model. This compression is designed to be lossless in terms of the information
conveyed, but it reduces the overall number of tokens used.

You can find the token limits for each model in the
[Google AI documentation](https://ai.google.dev/gemini-api/docs/models).