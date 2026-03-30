### Instrument code with traces

You can add traces to your own code for more detailed instrumentation.

Adding traces helps you debug and understand the flow of execution. Use the
`runInDevTraceSpan` function to wrap any section of code in a trace span.

Here is a basic example:

```typescript
import { runInDevTraceSpan } from '@google/gemini-cli-core';
import { GeminiCliOperation } from '@google/gemini-cli-core/lib/telemetry/constants.js';

await runInDevTraceSpan(
  {
    operation: GeminiCliOperation.ToolCall,
    attributes: {
      [GEN_AI_AGENT_NAME]: 'gemini-cli',
    },
  },
  async ({ metadata }) => {
    // metadata allows you to record the input and output of the
    // operation as well as other attributes.
    metadata.input = { key: 'value' };
    // Set custom attributes.
    metadata.attributes['custom.attribute'] = 'custom.value';

    // Your code to be traced goes here.
    try {
      const output = await somethingRisky();
      metadata.output = output;
      return output;
    } catch (e) {
      metadata.error = e;
      throw e;
    }
  },
);
```

In this example:

- `operation`: The operation type of the span, represented by the
  `GeminiCliOperation` enum.
- `metadata.input`: (Optional) An object containing the input data for the
  traced operation.
- `metadata.output`: (Optional) An object containing the output data from the
  traced operation.
- `metadata.attributes`: (Optional) A record of custom attributes to add to the
  span.
- `metadata.error`: (Optional) An error object to record if the operation fails.