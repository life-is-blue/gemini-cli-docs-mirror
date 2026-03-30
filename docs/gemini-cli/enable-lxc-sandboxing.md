# Enable LXC sandboxing
export GEMINI_SANDBOX=lxc
gemini -p "build the project"
```

**Custom container name**:

```bash
export GEMINI_SANDBOX=lxc
export GEMINI_SANDBOX_IMAGE=my-snapcraft-container
gemini -p "build the snap"
```

**Limitations**:

- Linux only (LXC is not available on macOS or Windows).
- The container must already exist and be running.
- The workspace directory is bind-mounted into the container at the same
  absolute path — the path must be writable inside the container.
- Used with tools like Snapcraft or Rockcraft that require a full system.