## Verify the result

After the edit is complete, verify the fix. You can simply read the file again
or, better yet, run your project's tests.

```none
`Run the tests for the UserProfile component.`
```

Gemini CLI uses the `run_shell_command` tool to execute your test runner (for
example, `npm test` or `jest`). This ensures the changes didn't break existing
functionality.