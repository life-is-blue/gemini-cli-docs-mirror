## Automatic saving

Your session history is recorded automatically as you interact with the model.
This background process ensures your work is preserved even if you interrupt a
session.

- **What is saved:** The complete conversation history, including:
  - Your prompts and the model's responses.
  - All tool executions (inputs and outputs).
  - Token usage statistics (input, output, cached, etc.).
  - Assistant thoughts and reasoning summaries (when available).
- **Location:** Sessions are stored in `~/.gemini/tmp/<project_hash>/chats/`,
  where `<project_hash>` is a unique identifier based on your project's root
  directory.
- **Scope:** Sessions are project-specific. Switching directories to a different
  project switches to that project's session history.