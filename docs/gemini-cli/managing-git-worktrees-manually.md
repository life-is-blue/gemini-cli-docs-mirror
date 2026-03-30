## Managing Git worktrees manually

For more control over worktree location and branch configuration, or to clean up
a preserved worktree, you can use Git directly:

- **Clean up a preserved Git worktree:**
  ```bash
  git worktree remove .gemini/worktrees/feature-search --force
  git branch -D worktree-feature-search
  ```
- **Create a Git worktree manually:**
  ```bash
  git worktree add ../project-feature-search -b feature-search
  cd ../project-feature-search && gemini
  ```

[Open an issue]: https://github.com/google-gemini/gemini-cli/issues