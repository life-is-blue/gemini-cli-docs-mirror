## Why combine Plan Mode and model steering?

[Plan Mode](/docs/cli/plan-mode) typically follows a linear path: research, propose,
and draft. Adding model steering lets you:

1.  **Direct the research:** Correct the agent if it's looking in the wrong
    directory or missing a key dependency.
2.  **Iterate mid-draft:** Suggest a different architectural pattern while the
    agent is still writing the plan.
3.  **Speed up the loop:** Avoid waiting for a full research turn to finish
    before providing critical context.