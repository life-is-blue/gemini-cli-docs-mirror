### 4. Ongoing triage for issues: `Scheduled Issue Triage`

This is a fallback workflow to ensure that no issue gets missed by the triage
process.

- **Workflow File**: `.github/workflows/gemini-scheduled-issue-triage.yml`
- **When it runs**: Every hour on all open issues.
- **What it does**:
  - It actively seeks out issues that either have no labels at all or still have
    the `status/need-triage` label.
  - It then triggers the same powerful Gemini-based analysis as the initial
    triage bot to apply the correct labels.
- **What you should do**:
  - You typically don't need to do anything. This workflow is a safety net to
    ensure every issue is eventually categorized, even if the initial triage
    fails.