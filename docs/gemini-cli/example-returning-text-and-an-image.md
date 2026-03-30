### Example: Returning text and an image

Here is an example of a valid JSON response from an MCP tool that returns both a
text description and an image:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Here is the logo you requested."
    },
    {
      "type": "image",
      "data": "BASE64_ENCODED_IMAGE_DATA_HERE",
      "mimeType": "image/png"
    },
    {
      "type": "text",
      "text": "The logo was created in 2025."
    }
  ]
}
```

When the Gemini CLI receives this response, it will:

1.  Extract all the text and combine it into a single `functionResponse` part
    for the model.
2.  Present the image data as a separate `inlineData` part.
3.  Provide a clean, user-friendly summary in the CLI, indicating that both text
    and an image were received.

This enables you to build sophisticated tools that can provide rich, multi-modal
context to the Gemini model.