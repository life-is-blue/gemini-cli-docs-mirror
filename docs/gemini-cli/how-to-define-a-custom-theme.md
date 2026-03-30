### How to define a custom theme

Add a `customThemes` block to your user, project, or system `settings.json`
file. Each custom theme is defined as an object with a unique name and a set of
nested configuration objects. For example:

```json
{
  "ui": {
    "customThemes": {
      "MyCustomTheme": {
        "name": "MyCustomTheme",
        "type": "custom",
        "background": {
          "primary": "#181818"
        },
        "text": {
          "primary": "#f0f0f0",
          "secondary": "#a0a0a0"
        }
      }
    }
  }
}
```

**Configuration objects:**

- **`text`**: Defines text colors.
  - `primary`: The default text color.
  - `secondary`: Used for less prominent text.
  - `link`: Color for URLs and links.
  - `accent`: Used for highlights and emphasis.
  - `response`: Precedence over `primary` for rendering model responses.
- **`background`**: Defines background colors.
  - `primary`: The main background color of the UI.
  - `diff.added`: Background for added lines in diffs.
  - `diff.removed`: Background for removed lines in diffs.
- **`border`**: Defines border colors.
  - `default`: The standard border color.
  - `focused`: Border color when an element is focused.
- **`status`**: Colors for status indicators.
  - `success`: Used for successful operations.
  - `warning`: Used for warnings.
  - `error`: Used for errors.
- **`ui`**: Other UI elements.
  - `comment`: Color for code comments.
  - `symbol`: Color for code symbols and operators.
  - `gradient`: An array of colors used for gradient effects.

**Required properties:**

- `name` (must match the key in the `customThemes` object and be a string)
- `type` (must be the string `"custom"`)

While all sub-properties are technically optional, we recommend providing at
least `background.primary`, `text.primary`, `text.secondary`, and the various
accent colors via `text.link`, `text.accent`, and `status` to ensure a cohesive
UI.

You can use either hex codes (e.g., `#FF0000`) **or** standard CSS color names
(e.g., `coral`, `teal`, `blue`) for any color value. See
[CSS color names](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#color_keywords)
for a full list of supported names.

You can define multiple custom themes by adding more entries to the
`customThemes` object.