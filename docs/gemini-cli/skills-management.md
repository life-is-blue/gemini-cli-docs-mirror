## Skills management

| Command                          | Description                           | Example                                           |
| -------------------------------- | ------------------------------------- | ------------------------------------------------- |
| `gemini skills list`             | List all discovered agent skills      | `gemini skills list`                              |
| `gemini skills install <source>` | Install skill from Git, path, or file | `gemini skills install https://github.com/u/repo` |
| `gemini skills link <path>`      | Link local agent skills via symlink   | `gemini skills link /path/to/my-skills`           |
| `gemini skills uninstall <name>` | Uninstall an agent skill              | `gemini skills uninstall my-skill`                |
| `gemini skills enable <name>`    | Enable an agent skill                 | `gemini skills enable my-skill`                   |
| `gemini skills disable <name>`   | Disable an agent skill                | `gemini skills disable my-skill`                  |
| `gemini skills enable --all`     | Enable all skills                     | `gemini skills enable --all`                      |
| `gemini skills disable --all`    | Disable all skills                    | `gemini skills disable --all`                     |

See [Agent Skills Documentation](/docs/cli/skills) for more details.