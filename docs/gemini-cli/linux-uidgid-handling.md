## Linux UID/GID handling

The sandbox automatically handles user permissions on Linux. Override these
permissions with:

**macOS/Linux**

```bash
export SANDBOX_SET_UID_GID=true   # Force host UID/GID
export SANDBOX_SET_UID_GID=false  # Disable UID/GID mapping
```

**Windows (PowerShell)**

```powershell
$env:SANDBOX_SET_UID_GID="true"   # Force host UID/GID
$env:SANDBOX_SET_UID_GID="false"  # Disable UID/GID mapping
```