## Method 1: Using npx

npx runs packages from a temporary cache without a permanent installation. To
"uninstall" the CLI, you must clear this cache, which will remove gemini-cli and
any other packages previously executed with npx.

The npx cache is a directory named `_npx` inside your main npm cache folder. You
can find your npm cache path by running `npm config get cache`.

**For macOS / Linux**

```bash