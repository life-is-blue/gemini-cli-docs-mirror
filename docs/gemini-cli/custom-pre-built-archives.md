### Custom pre-built archives

You can attach custom archives directly to your GitHub Release as assets. This
is useful if your extension requires a build step or includes platform-specific
binaries.

Custom archives must be fully self-contained and follow the required
[archive structure](#archive-structure). If your extension is
platform-independent, provide a single generic asset.

#### Platform-specific archives

To let Gemini CLI find the correct asset for a user's platform, use the
following naming convention:

1.  **Platform and architecture-specific:**
    `{platform}.{arch}.{name}.{extension}`
2.  **Platform-specific:** `{platform}.{name}.{extension}`
3.  **Generic:** A single asset will be used as a fallback if no specific match
    is found.

Use these values for the placeholders:

- `{name}`: Your extension name.
- `{platform}`: Use `darwin` (macOS), `linux`, or `win32` (Windows).
- `{arch}`: Use `x64` or `arm64`.
- `{extension}`: Use `.tar.gz` or `.zip`.

**Examples:**

- `darwin.arm64.my-tool.tar.gz` (specific to Apple Silicon Macs)
- `darwin.my-tool.tar.gz` (fallback for all Macs, e.g. Intel)
- `linux.x64.my-tool.tar.gz`
- `win32.my-tool.zip`

#### Archive structure

Archives must be fully contained extensions. The `gemini-extension.json` file
must be at the root of the archive. The rest of the layout should match a
standard extension structure.

#### Example GitHub Actions workflow

Use this example workflow to build and release your extension for multiple
platforms:

```yaml
name: Release Extension

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Build extension
        run: npm run build

      - name: Create release assets
        run: |
          npm run package -- --platform=darwin --arch=arm64
          npm run package -- --platform=linux --arch=x64
          npm run package -- --platform=win32 --arch=x64

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          files: |
            release/darwin.arm64.my-tool.tar.gz
            release/linux.arm64.my-tool.tar.gz
            release/win32.arm64.my-tool.zip
```