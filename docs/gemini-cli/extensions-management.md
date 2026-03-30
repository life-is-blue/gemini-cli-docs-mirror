## Extensions management

| Command                                            | Description                                  | Example                                                                        |
| -------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------ |
| `gemini extensions install <source>`               | Install extension from Git URL or local path | `gemini extensions install https://github.com/user/my-extension`               |
| `gemini extensions install <source> --ref <ref>`   | Install from specific branch/tag/commit      | `gemini extensions install https://github.com/user/my-extension --ref develop` |
| `gemini extensions install <source> --auto-update` | Install with auto-update enabled             | `gemini extensions install https://github.com/user/my-extension --auto-update` |
| `gemini extensions uninstall <name>`               | Uninstall one or more extensions             | `gemini extensions uninstall my-extension`                                     |
| `gemini extensions list`                           | List all installed extensions                | `gemini extensions list`                                                       |
| `gemini extensions update <name>`                  | Update a specific extension                  | `gemini extensions update my-extension`                                        |
| `gemini extensions update --all`                   | Update all extensions                        | `gemini extensions update --all`                                               |
| `gemini extensions enable <name>`                  | Enable an extension                          | `gemini extensions enable my-extension`                                        |
| `gemini extensions disable <name>`                 | Disable an extension                         | `gemini extensions disable my-extension`                                       |
| `gemini extensions link <path>`                    | Link local extension for development         | `gemini extensions link /path/to/extension`                                    |
| `gemini extensions new <path>`                     | Create new extension from template           | `gemini extensions new ./my-extension`                                         |
| `gemini extensions validate <path>`                | Validate extension structure                 | `gemini extensions validate ./my-extension`                                    |

See [Extensions Documentation](/docs/extensions) for more details.