## How to exit a Git worktree session

When you exit a worktree session (using `/quit` or `Ctrl+C`), Gemini leaves the
worktree intact so your work is not lost. This includes your uncommitted changes
(modified files, staged changes, or untracked files) and any new commits you
have made.

Gemini prioritizes a fast and safe exit: it **does not automatically delete**
your worktree or branch. You are responsible for cleaning up your worktrees
manually once you are finished with them.

When you exit, Gemini displays instructions on how to resume your work or how to
manually remove the worktree if you no longer need it.