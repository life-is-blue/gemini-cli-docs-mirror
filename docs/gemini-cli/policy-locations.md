### Policy locations

| Tier          | Type   | Location                                  |
| :------------ | :----- | :---------------------------------------- |
| **User**      | Custom | `~/.gemini/policies/*.toml`               |
| **Workspace** | Custom | `$WORKSPACE_ROOT/.gemini/policies/*.toml` |
| **Admin**     | System | _See below (OS specific)_                 |

#### System-wide policies (Admin)

Administrators can enforce system-wide policies (Tier 4) that override all user
and default settings. These policies can be loaded from standard system
locations or supplemental paths.

##### Standard Locations

These are the default paths the CLI searches for admin policies:

| OS          | Policy Directory Path                             |
| :---------- | :------------------------------------------------ |
| **Linux**   | `/etc/gemini-cli/policies`                        |
| **macOS**   | `/Library/Application Support/GeminiCli/policies` |
| **Windows** | `C:\ProgramData\gemini-cli\policies`              |

##### Supplemental Admin Policies

Administrators can also specify supplemental policy paths using:

- The `--admin-policy` command-line flag.
- The `adminPolicyPaths` setting in a system settings file.

These supplemental policies are assigned the same **Admin** tier (Base 4) as
policies in standard locations.

**Security Guard**: Supplemental admin policies are **ignored** if any `.toml`
policy files are found in the standard system location. This prevents flag-based
overrides when a central system policy has already been established.

#### Security Requirements

To prevent privilege escalation, the CLI enforces strict security checks on the
**standard system policy directory**. If checks fail, the policies in that
directory are **ignored**.

- **Linux / macOS:** Must be owned by `root` (UID 0) and NOT writable by group
  or others (e.g., `chmod 755`).
- **Windows:** Must be in `C:\ProgramData`. Standard users (`Users`, `Everyone`)
  must NOT have `Write`, `Modify`, or `Full Control` permissions. If you see a
  security warning, use the folder properties to remove write permissions for
  non-admin groups. You may need to "Disable inheritance" in Advanced Security
  Settings.

<!-- prettier-ignore -->
> [!NOTE]
> Supplemental admin policies (provided via `--admin-policy` or
> `adminPolicyPaths` settings) are **NOT** subject to these strict ownership
> checks, as they are explicitly provided by the user or administrator in their
> current execution context.