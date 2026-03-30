### Aliases (`customAliases`)

Aliases are named, reusable configuration presets. Users should define their own
aliases (or override system defaults) in the `customAliases` map.

- **Inheritance**: An alias can `extends` another alias (including system
  defaults like `chat-base`), inheriting its `modelConfig`. Child aliases can
  overwrite or augment inherited settings.
- **Abstract Aliases**: An alias is not required to specify a concrete `model`
  if it serves purely as a base for other aliases.

**Example Hierarchy**:

```json
"modelConfigs": {
  "customAliases": {
    "base": {
      "modelConfig": {
        "generateContentConfig": { "temperature": 0.0 }
      }
    },
    "chat-base": {
      "extends": "base",
      "modelConfig": {
        "generateContentConfig": { "temperature": 0.7 }
      }
    }
  }
}
```