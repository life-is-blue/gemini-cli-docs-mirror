### Sandboxing

#### macOS Seatbelt

On macOS, `gemini` uses Seatbelt (`sandbox-exec`) under a `permissive-open`
profile (see `packages/cli/src/utils/sandbox-macos-permissive-open.sb`) that
restricts writes to the project folder but otherwise allows all other operations
and outbound network traffic ("open") by default. You can switch to a
`strict-open` profile (see
`packages/cli/src/utils/sandbox-macos-strict-open.sb`) that restricts both reads
and writes to the working directory while allowing outbound network traffic by
setting `SEATBELT_PROFILE=strict-open` in your environment or `.env` file.
Available built-in profiles are `permissive-{open,proxied}`,
`restrictive-{open,proxied}`, and `strict-{open,proxied}` (see below for proxied
networking). You can also switch to a custom profile
`SEATBELT_PROFILE=<profile>` if you also create a file
`.gemini/sandbox-macos-<profile>.sb` under your project settings directory
`.gemini`.

#### Container-based sandboxing (all platforms)

For stronger container-based sandboxing on macOS or other platforms, you can set
`GEMINI_SANDBOX=true|docker|podman|<command>` in your environment or `.env`
file. The specified command (or if `true` then either `docker` or `podman`) must
be installed on the host machine. Once enabled, `npm run build:all` will build a
minimal container ("sandbox") image and `npm start` will launch inside a fresh
instance of that container. The first build can take 20-30s (mostly due to
downloading of the base image) but after that both build and start overhead
should be minimal. Default builds (`npm run build`) will not rebuild the
sandbox.

Container-based sandboxing mounts the project directory (and system temp
directory) with read-write access and is started/stopped/removed automatically
as you start/stop Gemini CLI. Files created within the sandbox should be
automatically mapped to your user/group on host machine. You can easily specify
additional mounts, ports, or environment variables by setting
`SANDBOX_{MOUNTS,PORTS,ENV}` as needed. You can also fully customize the sandbox
for your projects by creating the files `.gemini/sandbox.Dockerfile` and/or
`.gemini/sandbox.bashrc` under your project settings directory (`.gemini`) and
running `gemini` with `BUILD_SANDBOX=1` to trigger building of your custom
sandbox.

#### Proxied networking

All sandboxing methods, including macOS Seatbelt using `*-proxied` profiles,
support restricting outbound network traffic through a custom proxy server that
can be specified as `GEMINI_SANDBOX_PROXY_COMMAND=<command>`, where `<command>`
must start a proxy server that listens on `:::8877` for relevant requests. See
`docs/examples/proxy-script.md` for a minimal proxy that only allows `HTTPS`
connections to `example.com:443` (e.g. `curl https://example.com`) and declines
all other requests. The proxy is started and stopped automatically alongside the
sandbox.