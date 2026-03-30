### Loading themes from a file

In addition to defining custom themes in `settings.json`, you can also load a
theme directly from a JSON file by specifying the file path in your
`settings.json`. This is useful for sharing themes or keeping them separate from
your main configuration.

To load a theme from a file, set the `theme` property in your `settings.json` to
the path of your theme file:

```json
{
  "ui": {
    "theme": "/path/to/your/theme.json"
  }
}
```

The theme file must be a valid JSON file that follows the same structure as a
custom theme defined in `settings.json`.

**Example `my-theme.json`:**

```json
{
  "name": "Gruvbox Dark",
  "type": "custom",
  "background": {
    "primary": "#282828",
    "diff": {
      "added": "#2b3312",
      "removed": "#341212"
    }
  },
  "text": {
    "primary": "#ebdbb2",
    "secondary": "#a89984",
    "link": "#83a598",
    "accent": "#d3869b"
  },
  "border": {
    "default": "#3c3836",
    "focused": "#458588"
  },
  "status": {
    "success": "#b8bb26",
    "warning": "#fabd2f",
    "error": "#fb4934"
  },
  "ui": {
    "comment": "#928374",
    "symbol": "#8ec07c",
    "gradient": ["#cc241d", "#d65d0e", "#d79921"]
  }
}
```

<!-- prettier-ignore -->
> [!WARNING]
> For your safety, Gemini CLI will only load theme files that
> are located within your home directory. If you attempt to load a theme from
> outside your home directory, a warning will be displayed and the theme will
> not be loaded. This is to prevent loading potentially malicious theme files
> from untrusted sources.