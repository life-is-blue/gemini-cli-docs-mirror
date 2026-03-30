## Step 2: Steer the research phase

As you see the agent calling tools like `list_directory` or `grep_search`, you
might realize it's missing the relevant context.

**Action:** While the spinner is active, type your hint:
`"Don't forget to check packages/common/queues for the existing Redis config."`

**Result:** Gemini CLI acknowledges your hint and immediately incorporates it
into its research. You'll see it start exploring the directory you suggested in
its very next turn.