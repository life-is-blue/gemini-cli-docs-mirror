# [Gemini CLI settings (`/settings` command)](http://geminicli.com/docs/cli/settings.md)


Control your Gemini CLI experience with the `/settings` command. The `/settings`
command opens a dialog to view and edit all your Gemini CLI settings, including
your UI experience, keybindings, and accessibility features.

Your Gemini CLI settings are stored in a `settings.json` file. In addition to
using the `/settings` command, you can also edit them in one of the following
locations:

- **User settings**: `~/.gemini/settings.json`
- **Workspace settings**: `your-project/.gemini/settings.json`

<!-- prettier-ignore -->
> [!IMPORTANT]
> Workspace settings override user settings.