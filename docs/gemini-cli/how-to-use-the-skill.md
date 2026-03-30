## How to use the skill

Now, try it out. Start a new session and ask a question that triggers the
skill's description.

**User:** "Can you audit http://geminicli.com"

Gemini recognizes the request matches the `api-auditor` description and asks for
permission to activate it.

**Model:** (After calling `activate_skill`) "I've activated the **api-auditor**
skill. I'll run the audit script now..."

Gemini then uses the `run_shell_command` tool to execute your bundled Node
script:

`node .gemini/skills/api-auditor/scripts/audit.js http://geminili.com`