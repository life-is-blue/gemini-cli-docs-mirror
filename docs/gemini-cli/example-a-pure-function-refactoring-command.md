## Example: A "Pure Function" refactoring command

Let's create a global command that asks the model to refactor a piece of code.

**1. Create the file and directories:**

First, ensure the user commands directory exists, then create a `refactor`
subdirectory for organization and the final TOML file.

**macOS/Linux**

```bash
mkdir -p ~/.gemini/commands/refactor
touch ~/.gemini/commands/refactor/pure.toml
```

**Windows (PowerShell)**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.gemini\commands\refactor"
New-Item -ItemType File -Force -Path "$env:USERPROFILE\.gemini\commands\refactor\pure.toml"
```

**2. Add the content to the file:**

Open `~/.gemini/commands/refactor/pure.toml` in your editor and add the
following content. We are including the optional `description` for best
practice.

```toml