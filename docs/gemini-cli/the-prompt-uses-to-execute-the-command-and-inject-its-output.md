# The prompt uses !{...} to execute the command and inject its output.
prompt = """
Please generate a Conventional Commit message based on the following git diff:

```diff
!{git diff --staged}
```

"""

````

When you run `/git:commit`, the CLI first executes `git diff --staged`, then
replaces `!{git diff --staged}` with the output of that command before sending
the final, complete prompt to the model.