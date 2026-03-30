### Blocklisting with `excludeTools` (Deprecated)

> **Deprecated:** Use the [Policy Engine](/docs/reference/policy-engine) for
> more robust control.

Alternatively, you can add specific tools that are considered dangerous in your
environment to a blocklist.

**Example:** Prevent the use of the shell tool for removing files.

```json
{
  "tools": {
    "exclude": ["ShellTool(rm -rf)"]
  }
}
```

<!-- prettier-ignore -->
> [!WARNING]
> Blocklisting with `excludeTools` is less secure than
> allowlisting with `coreTools`, as it relies on blocking known-bad commands,
> and clever users may find ways to bypass simple string-based blocks.
> **Allowlisting is the recommended approach.**