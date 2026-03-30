# [Git Worktrees (experimental)](http://geminicli.com/docs/cli/git-worktrees.md)


When working on multiple tasks at once, you can use Git worktrees to give each
Gemini session its own copy of the codebase. Git worktrees create separate
working directories that each have their own files and branch while sharing the
same repository history. This prevents changes in one session from colliding
with another.

Learn more about [session management](/docs/cli/session-management).

<!-- prettier-ignore -->
> [!NOTE]
> This is an experimental feature currently under active development. Your
> feedback is invaluable as we refine this feature. If you have ideas,
> suggestions, or encounter issues:
>
> - [Open an issue](https://github.com/google-gemini/gemini-cli/issues/new?template=bug_report.yml) on GitHub.
> - Use the **/bug** command within Gemini CLI to file an issue.

Learn more in the official Git worktree
[documentation](https://git-scm.com/docs/git-worktree).