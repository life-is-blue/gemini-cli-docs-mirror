## Configuration

Hooks are configured in `settings.json`. Gemini CLI merges configurations from
multiple layers in the following order of precedence (highest to lowest):

1.  **Project settings**: `.gemini/settings.json` in the current directory.
2.  **User settings**: `~/.gemini/settings.json`.
3.  **System settings**: `/etc/gemini-cli/settings.json`.
4.  **Extensions**: Hooks defined by installed extensions.