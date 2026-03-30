### 3. Ongoing triage for pull requests: `PR Auditing and Label Sync`

This workflow runs periodically to ensure all open PRs are correctly linked to
issues and have consistent labels.

- **Workflow File**: `.github/workflows/gemini-scheduled-pr-triage.yml`
- **When it runs**: Every 15 minutes on all open pull requests.
- **What it does**:
  - **Checks for a linked issue**: The bot scans your PR description for a
    keyword that links it to an issue (e.g., `Fixes #123`, `Closes #456`).
  - **Adds `status/need-issue`**: If no linked issue is found, the bot will add
    the `status/need-issue` label to your PR. This is a clear signal that an
    issue needs to be created and linked.
  - **Synchronizes labels**: If an issue _is_ linked, the bot ensures the PR's
    labels perfectly match the issue's labels. It will add any missing labels
    and remove any that don't belong, and it will remove the `status/need-issue`
    label if it was present.
- **What you should do**:
  - **Always link your PR to an issue.** This is the most important step. Add a
    line like `Resolves #<issue-number>` to your PR description.
  - This will ensure your PR is correctly categorized and moves through the
    review process smoothly.