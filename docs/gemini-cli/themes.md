### Themes

Extensions can provide custom themes to personalize the CLI UI. Themes are
defined in the `themes` array in `gemini-extension.json`.

**Example**

```json
{
  "name": "my-green-extension",
  "version": "1.0.0",
  "themes": [
    {
      "name": "shades-of-green",
      "type": "custom",
      "background": {
        "primary": "#1a362a"
      },
      "text": {
        "primary": "#a6e3a1",
        "secondary": "#6e8e7a",
        "link": "#89e689"
      },
      "status": {
        "success": "#76c076",
        "warning": "#d9e689",
        "error": "#b34e4e"
      },
      "border": {
        "default": "#4a6c5a"
      },
      "ui": {
        "comment": "#6e8e7a"
      }
    }
  ]
}
```

Custom themes provided by extensions can be selected using the `/theme` command
or by setting the `ui.theme` property in your `settings.json` file. Note that
when referring to a theme from an extension, the extension name is appended to
the theme name in parentheses, e.g., `shades-of-green (my-green-extension)`.