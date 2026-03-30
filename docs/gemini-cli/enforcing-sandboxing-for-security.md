## Enforcing sandboxing for security

To mitigate the risk of potentially harmful operations, you can enforce the use
of sandboxing for all tool execution. The sandbox isolates tool execution in a
containerized environment.

**Example:** Force all tool execution to happen within a Docker sandbox.

```json
{
  "tools": {
    "sandbox": "docker"
  }
}
```

You can also specify a custom, hardened Docker image for the sandbox by building
a custom `sandbox.Dockerfile` as described in the
[Sandboxing documentation](/docs/cli/sandbox).