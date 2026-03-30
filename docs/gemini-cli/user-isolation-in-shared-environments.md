## User isolation in shared environments

In shared compute environments (like ML experiment runners or shared build
servers), you can isolate Gemini CLI state by overriding the user's home
directory.

By default, Gemini CLI stores configuration and history in `~/.gemini`. You can
use the `GEMINI_CLI_HOME` environment variable to point to a unique directory
for a specific user or job. The CLI will create a `.gemini` folder inside the
specified path.

**macOS/Linux**

```bash