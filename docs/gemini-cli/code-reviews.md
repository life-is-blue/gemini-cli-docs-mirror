### Code reviews

All submissions, including submissions by project members, require review. We
use [GitHub pull requests](https://docs.github.com/articles/about-pull-requests)
for this purpose.

To assist with the review process, we provide an automated review tool that
helps detect common anti-patterns, testing issues, and other best practices that
are easy to miss.

#### Using the automated review tool

You can run the review tool in two ways:

1.  **Using the helper script (Recommended):** We provide a script that
    automatically handles checking out the PR into a separate worktree,
    installing dependencies, building the project, and launching the review
    tool.

    ```bash
    ./scripts/review.sh <PR_NUMBER> [model]
    ```

    **Warning:** If you run `scripts/review.sh`, you must have first verified
    that the code for the PR being reviewed is safe to run and does not contain
    data exfiltration attacks.

    **Authors are strongly encouraged to run this script on their own PRs**
    immediately after creation. This allows you to catch and fix simple issues
    locally before a maintainer performs a full review.

    **Note on Models:** By default, the script uses the latest Pro model
    (`gemini-3.1-pro-preview`). If you do not have enough Pro quota, you can run
    it with the latest Flash model instead:
    `./scripts/review.sh <PR_NUMBER> gemini-3-flash-preview`.

2.  **Manually from within Gemini CLI:** If you already have the PR checked out
    and built, you can run the tool directly from the CLI prompt:

    ```text
    /review-frontend <PR_NUMBER>
    ```

Replace `<PR_NUMBER>` with your pull request number. Reviewers should use this
tool to augment, not replace, their manual review process.