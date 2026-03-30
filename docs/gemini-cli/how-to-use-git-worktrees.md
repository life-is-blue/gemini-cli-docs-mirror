## How to use Git worktrees

Use the `--worktree` (`-w`) flag to create an isolated worktree and start Gemini
CLI in it.

- **Start with a specific name:** The value you pass becomes both the directory
  name (within `.gemini/worktrees/`) and the branch name.

  ```bash
  gemini --worktree feature-search
  ```

- **Start with a random name:** If you omit the name, Gemini generates a random
  one automatically (for example, `worktree-a1b2c3d4`).

  ```bash
  gemini --worktree
  ```

<!-- prettier-ignore -->
> [!NOTE]
> Remember to initialize your development environment in each new
> worktree according to your project's setup. Depending on your stack, this
> might include running dependency installation (`npm install`, `yarn`), setting
> up virtual environments, or following your project's standard build process.