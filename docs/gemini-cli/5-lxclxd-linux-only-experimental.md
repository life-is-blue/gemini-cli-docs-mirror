### 5. LXC/LXD (Linux only, experimental)

Full-system container sandboxing using LXC/LXD. Unlike Docker/Podman, LXC
containers run a complete Linux system with `systemd`, `snapd`, and other system
services. This is ideal for tools that don't work in standard Docker containers,
such as Snapcraft and Rockcraft.

**Prerequisites**:

- Linux only.
- LXC/LXD must be installed (`snap install lxd` or `apt install lxd`).
- A container must be created and running before starting Gemini CLI. Gemini
  does **not** create the container automatically.

**Quick setup**:

```bash