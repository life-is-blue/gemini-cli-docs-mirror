### Telemetry

For more detailed telemetry, you can use the following environment variables to
capture telemetry data to a file:

- `GEMINI_TELEMETRY_ENABLED=true`
- `GEMINI_TELEMETRY_TARGET=local`
- `GEMINI_TELEMETRY_OUTFILE=/path/to/your/log.json`

This will write a JSON log file containing detailed information about all the
events happening within the agent, including ACP requests and responses. The
integration test `integration-tests/acp-telemetry.test.ts` provides a working
example of how to set this up.