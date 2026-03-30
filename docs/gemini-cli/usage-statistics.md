## Usage statistics

To help us improve the Gemini CLI, we collect anonymized usage statistics. This
data helps us understand how the CLI is used, identify common issues, and
prioritize new features.

**What we collect:**

- **Tool calls:** We log the names of the tools that are called, whether they
  succeed or fail, and how long they take to execute. We do not collect the
  arguments passed to the tools or any data returned by them.
- **API requests:** We log the Gemini model used for each request, the duration
  of the request, and whether it was successful. We do not collect the content
  of the prompts or responses.
- **Session information:** We collect information about the configuration of the
  CLI, such as the enabled tools and the approval mode.

**What we DON'T collect:**

- **Personally identifiable information (PII):** We do not collect any personal
  information, such as your name, email address, or API keys.
- **Prompt and response content:** We do not log the content of your prompts or
  the responses from the Gemini model.
- **File content:** We do not log the content of any files that are read or
  written by the CLI.

**How to opt out:**

You can opt out of usage statistics collection at any time by setting the
`usageStatisticsEnabled` property to `false` under the `privacy` category in
your `settings.json` file:

```json
{
  "privacy": {
    "usageStatisticsEnabled": false
  }
}
```