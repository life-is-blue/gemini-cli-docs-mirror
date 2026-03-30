### Setting the pager

You can set a custom pager for the shell output by setting the
`tools.shell.pager` setting. The default pager is `cat`. This setting only
applies when `tools.shell.enableInteractiveShell` is enabled.

**Example `settings.json`:**

```json
{
  "tools": {
    "shell": {
      "pager": "less"
    }
  }
}
```