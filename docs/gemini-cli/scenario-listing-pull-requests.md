### Scenario: Listing pull requests

**Prompt:** `List the open PRs in the google/gemini-cli repository.`

The agent will:

1.  Recognize the request matches a GitHub tool.
2.  Call `mcp_github_list_pull_requests`.
3.  Present the data to you.