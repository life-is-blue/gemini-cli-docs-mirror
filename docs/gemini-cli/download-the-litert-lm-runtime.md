### Download the LiteRT-LM runtime

The [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) runtime offers
pre-built binaries for locally-serving models. Download the binary appropriate
for your system.

#### Windows

1. Download
   [lit.windows_x86_64.exe](https://github.com/google-ai-edge/LiteRT-LM/releases/download/v0.9.0-alpha03/lit.windows_x86_64.exe).
2. Using GPU on Windows requires the DirectXShaderCompiler. Download the
   [dxc zip from the latest release](https://github.com/microsoft/DirectXShaderCompiler/releases/download/v1.8.2505.1/dxc_2025_07_14.zip).
   Unzip the archive and from the architecture-appropriate `bin\` directory, and
   copy the `dxil.dll` and `dxcompiler.dll` into the same location as you saved
   `lit.windows_x86_64.exe`.
3. (Optional) Test starting the runtime:
   `.\lit.windows_x86_64.exe serve --verbose`

#### Linux

1. Download
   [lit.linux_x86_64](https://github.com/google-ai-edge/LiteRT-LM/releases/download/v0.9.0-alpha03/lit.linux_x86_64).
2. Ensure the binary is executable: `chmod a+x lit.linux_x86_64`
3. (Optional) Test starting the runtime: `./lit.linux_x86_64 serve --verbose`

#### MacOS

1. Download
   [lit-macos-arm64](https://github.com/google-ai-edge/LiteRT-LM/releases/download/v0.9.0-alpha03/lit.macos_arm64).
2. Ensure the binary is executable: `chmod a+x lit.macos_arm64`
3. (Optional) Test starting the runtime: `./lit.macos_arm64 serve --verbose`

> **Note**: MacOS can be configured to only allows binaries from "App Store &
> Known Developers". If you encounter an error message when attempting to run
> the binary, you will need to allow the application. One option is to visit
> `System Settings -> Privacy & Security`, scroll to `Security`, and click
> `"Allow Anyway"` for `"lit.macos_arm64"`. Another option is to run
> `xattr -d com.apple.quarantine lit.macos_arm64` from the commandline.