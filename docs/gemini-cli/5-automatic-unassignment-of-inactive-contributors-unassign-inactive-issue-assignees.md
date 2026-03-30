### 5. Automatic unassignment of inactive contributors: `Unassign Inactive Issue Assignees`

To keep the list of open `help wanted` issues accessible to all contributors,
this workflow automatically removes **external contributors** who have not
opened a linked pull request within **7 days** of being assigned. Maintainers,
org members, and repo collaborators with write access or above are always exempt
and will never be auto-unassigned.

- **Workflow File**: `.github/workflows/unassign-inactive-assignees.yml`
- **When it runs**: Every day at 09:00 UTC, and can be triggered manually with
  an optional `dry_run` mode.
- **What it does**:
  1. Finds every open issue labeled `help wanted` that has at least one
     assignee.
  2. Identifies privileged users (team members, repo collaborators with write+
     access, maintainers) and skips them entirely.
  3. For each remaining (external) assignee it reads the issue's timeline to
     determine:
     - The exact date they were assigned (using `assigned` timeline events).
     - Whether they have opened a PR that is already linked/cross-referenced to
       the issue.
  4. Each cross-referenced PR is fetched to verify it is **ready for review**:
     open and non-draft, or already merged. Draft PRs do not count.
  5. If an assignee has been assigned for **more than 7 days** and no qualifying
     PR is found, they are automatically unassigned and a comment is posted
     explaining the reason and how to re-claim the issue.
  6. Assignees who have a non-draft, open or merged PR linked to the issue are
     **never** unassigned by this workflow.
- **What you should do**:
  - **Open a real PR, not a draft**: Within 7 days of being assigned, open a PR
    that is ready for review and include `Fixes #<issue-number>` in the
    description. Draft PRs do not satisfy the requirement and will not prevent
    auto-unassignment.
  - **Re-assign if unassigned by mistake**: Comment `/assign` on the issue to
    assign yourself again.
  - **Unassign yourself** if you can no longer work on the issue by commenting
    `/unassign`, so other contributors can pick it up right away.