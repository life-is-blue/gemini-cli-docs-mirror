### Automatic delegation

Gemini CLI's main agent is instructed to use specialized subagents when a task
matches their expertise. For example, if you ask "How does the auth system
work?", the main agent may decide to call the `codebase_investigator` subagent
to perform the research.