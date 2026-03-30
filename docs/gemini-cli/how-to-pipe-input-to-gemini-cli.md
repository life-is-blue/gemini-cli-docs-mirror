## How to pipe input to Gemini CLI

Feed data into Gemini using the standard Unix pipe `|`. Gemini reads the
standard input (stdin) as context and answers your question using standard
output.

Pipe a file:

**macOS/Linux**

```bash
cat error.log | gemini -p "Explain why this failed"
```

**Windows (PowerShell)**

```powershell
Get-Content error.log | gemini -p "Explain why this failed"
```

Pipe a command:

```bash
git diff | gemini -p "Write a commit message for these changes"
```