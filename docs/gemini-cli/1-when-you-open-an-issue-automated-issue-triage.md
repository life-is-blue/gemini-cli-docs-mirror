### 1. When you open an issue: `Automated Issue Triage`

This is the first bot you will interact with when you create an issue. Its job
is to perform an initial analysis and apply the correct labels.

- **Workflow File**: `.github/workflows/gemini-automated-issue-triage.yml`
- **When it runs**: Immediately after an issue is created or reopened.
- **What it does**:
  - It uses a Gemini model to analyze the issue's title and body against a
    detailed set of guidelines.
  - **Applies one `area/*` label**: Categorizes the issue into a functional area
    of the project (e.g., `area/ux`, `area/models`, `area/platform`).
  - **Applies one `kind/*` label**: Identifies the type of issue (e.g.,
    `kind/bug`, `kind/enhancement`, `kind/question`).
  - **Applies one `priority/*` label**: Assigns a priority from P0 (critical) to
    P3 (low) based on the described impact.
  - **May apply `status/need-information`**: If the issue lacks critical details
    (like logs or reproduction steps), it will be flagged for more information.
  - **May apply `status/need-retesting`**: If the issue references a CLI version
    that is more than six versions old, it will be flagged for retesting on a
    current version.
- **What you should do**:
  - Fill out the issue template as completely as possible. The more detail you
    provide, the more accurate the triage will be.
  - If the `status/need-information` label is added, please provide the
    requested details in a comment.