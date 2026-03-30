### Log to files

Since hooks run in the background, writing to a dedicated log file is often the
easiest way to debug complex logic.

```bash
#!/usr/bin/env bash
LOG_FILE=".gemini/hooks/debug.log"