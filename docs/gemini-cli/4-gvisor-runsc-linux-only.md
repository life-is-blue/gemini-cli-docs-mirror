### 4. gVisor / runsc (Linux only)

Strongest isolation available: runs containers inside a user-space kernel via
[gVisor](https://github.com/google/gvisor). gVisor intercepts all container
system calls and handles them in a sandboxed kernel written in Go, providing a
strong security barrier between AI operations and the host OS.

**Prerequisites:**

- Linux (gVisor supports Linux only)
- Docker installed and running
- gVisor/runsc runtime configured

When you set `sandbox: "runsc"`, Gemini CLI runs
`docker run --runtime=runsc ...` to execute containers with gVisor isolation.
runsc is not auto-detected; you must specify it explicitly (e.g.
`GEMINI_SANDBOX=runsc` or `sandbox: "runsc"`).

To set up runsc:

1.  Install the runsc binary.
2.  Configure the Docker daemon to use the runsc runtime.
3.  Verify the installation.