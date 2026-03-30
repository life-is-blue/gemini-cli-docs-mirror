### Configuration Format

The configuration uses a JSON array of objects, similar to VS Code's keybinding
schema. Each object must specify a `command` from the reference tables above and
a `key` combination.

```json
[
  {
    "command": "edit.clear",
    "key": "cmd+l"
  },
  {
    // prefix "-" to unbind a key
    "command": "-app.toggleYolo",
    "key": "ctrl+y"
  },
  {
    "command": "input.submit",
    "key": "ctrl+y"
  },
  {
    // multiple modifiers
    "command": "cursor.right",
    "key": "shift+alt+a"
  },
  {
    // Some mac keyboards send "Å" instead of "shift+option+a"
    "command": "cursor.right",
    "key": "Å"
  },
  {
    // some base keys have special multi-char names
    "command": "cursor.right",
    "key": "shift+pageup"
  }
]
```

- **Unbinding** To remove an existing or default keybinding, prefix a minus sign
  (`-`) to the `command` name.
- **No Auto-unbinding** The same key can be bound to multiple commands in
  different contexts at the same time. Therefore, creating a binding does not
  automatically unbind the key from other commands.
- **Explicit Modifiers**: Key matching is explicit. For example, a binding for
  `ctrl+f` will only trigger on exactly `ctrl+f`, not `ctrl+shift+f` or
  `alt+ctrl+f`.
- **Literal Characters**: Terminals often translate complex key combinations
  (especially on macOS with the `Option` key) into special characters, losing
  modifier and keystroke information along the way. For example,`shift+5` might
  be sent as `%`. In these cases, you must bind to the literal character `%` as
  bindings to `shift+5` will never fire. To see precisely what is being sent,
  enable `Debug Keystroke Logging` and hit f12 to open the debug log console.
- **Key Modifiers**: The supported key modifiers are:
  - `ctrl`
  - `shift`,
  - `alt` (synonyms: `opt`, `option`)
  - `cmd` (synonym: `meta`)
- **Base Key**: The base key can be any single unicode code point or any of the
  following special keys:
  - **Navigation**: `up`, `down`, `left`, `right`, `home`, `end`, `pageup`,
    `pagedown`
  - **Actions**: `enter`, `escape`, `tab`, `space`, `backspace`, `delete`,
    `clear`, `insert`, `printscreen`
  - **Toggles**: `capslock`, `numlock`, `scrolllock`, `pausebreak`
  - **Function Keys**: `f1` through `f35`
  - **Numpad**: `numpad0` through `numpad9`, `numpad_add`, `numpad_subtract`,
    `numpad_multiply`, `numpad_divide`, `numpad_decimal`, `numpad_separator`