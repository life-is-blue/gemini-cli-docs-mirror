### Custom sandbox flags

For container-based sandboxing, you can inject custom flags into the `docker` or
`podman` command using the `SANDBOX_FLAGS` environment variable. This is useful
for advanced configurations, such as disabling security features for specific
use cases.

**Example (Podman)**:

To disable SELinux labeling for volume mounts, you can set the following:

**macOS/Linux**

```bash
export SANDBOX_FLAGS="--security-opt label=disable"
```

**Windows (PowerShell)**

```powershell
$env:SANDBOX_FLAGS="--security-opt label=disable"
```

Multiple flags can be provided as a space-separated string:

**macOS/Linux**

```bash
export SANDBOX_FLAGS="--flag1 --flag2=value"
```

**Windows (PowerShell)**

```powershell
$env:SANDBOX_FLAGS="--flag1 --flag2=value"
```