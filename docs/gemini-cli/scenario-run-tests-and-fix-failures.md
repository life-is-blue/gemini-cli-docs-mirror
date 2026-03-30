### Scenario: Run tests and fix failures

You want to run tests and fix any failures.

**Prompt:**
`Run the unit tests. If any fail, analyze the error and try to fix the code.`

**Workflow:**

1.  Gemini calls `run_shell_command('npm test')`.
2.  You see a confirmation prompt: `Allow command 'npm test'? [y/N]`.
3.  You press `y`.
4.  The tests run. If they fail, Gemini reads the error output.
5.  Gemini uses `read_file` to inspect the failing test.
6.  Gemini uses `replace` to fix the bug.
7.  Gemini runs `npm test` again to verify the fix.

This loop lets Gemini work autonomously.