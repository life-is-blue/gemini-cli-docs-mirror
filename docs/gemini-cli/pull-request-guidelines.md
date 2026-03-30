### Pull request guidelines

To help us review and merge your PRs quickly, please follow these guidelines.
PRs that do not meet these standards may be closed.

#### 1. Link to an existing issue

All PRs should be linked to an existing issue in our tracker. This ensures that
every change has been discussed and is aligned with the project's goals before
any code is written.

- **For bug fixes:** The PR should be linked to the bug report issue.
- **For features:** The PR should be linked to the feature request or proposal
  issue that has been approved by a maintainer.

If an issue for your change doesn't exist, we will automatically close your PR
along with a comment reminding you to associate the PR with an issue. The ideal
workflow starts with an issue that has been reviewed and approved by a
maintainer. Please **open the issue first** and wait for feedback before you
start coding.

#### 2. Keep it small and focused

We favor small, atomic PRs that address a single issue or add a single,
self-contained feature.

- **Do:** Create a PR that fixes one specific bug or adds one specific feature.
- **Don't:** Bundle multiple unrelated changes (e.g., a bug fix, a new feature,
  and a refactor) into a single PR.

Large changes should be broken down into a series of smaller, logical PRs that
can be reviewed and merged independently.

#### 3. Use draft PRs for work in progress

If you'd like to get early feedback on your work, please use GitHub's **Draft
Pull Request** feature. This signals to the maintainers that the PR is not yet
ready for a formal review but is open for discussion and initial feedback.

#### 4. Ensure all checks pass

Before submitting your PR, ensure that all automated checks are passing by
running `npm run preflight`. This command runs all tests, linting, and other
style checks.

#### 5. Update documentation

If your PR introduces a user-facing change (e.g., a new command, a modified
flag, or a change in behavior), you must also update the relevant documentation
in the `/docs` directory.

See more about writing documentation:
[Documentation contribution process](#documentation-contribution-process).

#### 6. Write clear commit messages and a good PR description

Your PR should have a clear, descriptive title and a detailed description of the
changes. Follow the [Conventional Commits](https://www.conventionalcommits.org/)
standard for your commit messages.

- **Good PR title:** `feat(cli): Add --json flag to 'config get' command`
- **Bad PR title:** `Made some changes`

In the PR description, explain the "why" behind your changes and link to the
relevant issue (e.g., `Fixes #123`).