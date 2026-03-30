## Authentication

You can enforce a specific authentication method for all users by setting the
`enforcedAuthType` in the system-level `settings.json` file. This prevents users
from choosing a different authentication method. See the
[Authentication docs](/docs/get-started/authentication) for more details.

**Example:** Enforce the use of Google login for all users.

```json
{
  "enforcedAuthType": "oauth-personal"
}
```

If a user has a different authentication method configured, they will be
prompted to switch to the enforced method. In non-interactive mode, the CLI will
exit with an error if the configured authentication method does not match the
enforced one.