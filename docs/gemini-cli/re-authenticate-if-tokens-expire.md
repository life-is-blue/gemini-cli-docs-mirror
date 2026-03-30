# Re-authenticate if tokens expire
/mcp auth serverName
```

#### OAuth configuration properties

- **`enabled`** (boolean): Enable OAuth for this server
- **`clientId`** (string): OAuth client identifier (optional with dynamic
  registration)
- **`clientSecret`** (string): OAuth client secret (optional for public clients)
- **`authorizationUrl`** (string): OAuth authorization endpoint (auto-discovered
  if omitted)
- **`tokenUrl`** (string): OAuth token endpoint (auto-discovered if omitted)
- **`scopes`** (string[]): Required OAuth scopes
- **`redirectUri`** (string): Custom redirect URI (defaults to
  `http://localhost:7777/oauth/callback`)
- **`tokenParamName`** (string): Query parameter name for tokens in SSE URLs
- **`audiences`** (string[]): Audiences the token is valid for

#### Token management

OAuth tokens are automatically:

- **Stored securely** in `~/.gemini/mcp-oauth-tokens.json`
- **Refreshed** when expired (if refresh tokens are available)
- **Validated** before each connection attempt
- **Cleaned up** when invalid or expired

#### Authentication provider type

You can specify the authentication provider type using the `authProviderType`
property:

- **`authProviderType`** (string): Specifies the authentication provider. Can be
  one of the following:
  - **`dynamic_discovery`** (default): The CLI will automatically discover the
    OAuth configuration from the server.
  - **`google_credentials`**: The CLI will use the Google Application Default
    Credentials (ADC) to authenticate with the server. When using this provider,
    you must specify the required scopes.
  - **`service_account_impersonation`**: The CLI will impersonate a Google Cloud
    Service Account to authenticate with the server. This is useful for
    accessing IAP-protected services (this was specifically designed for Cloud
    Run services).

#### Google credentials

```json
{
  "mcpServers": {
    "googleCloudServer": {
      "httpUrl": "https://my-gcp-service.run.app/mcp",
      "authProviderType": "google_credentials",
      "oauth": {
        "scopes": ["https://www.googleapis.com/auth/userinfo.email"]
      }
    }
  }
}
```

#### Service account impersonation

To authenticate with a server using Service Account Impersonation, you must set
the `authProviderType` to `service_account_impersonation` and provide the
following properties:

- **`targetAudience`** (string): The OAuth Client ID allowlisted on the
  IAP-protected application you are trying to access.
- **`targetServiceAccount`** (string): The email address of the Google Cloud
  Service Account to impersonate.

The CLI will use your local Application Default Credentials (ADC) to generate an
OIDC ID token for the specified service account and audience. This token will
then be used to authenticate with the MCP server.

#### Setup instructions

1. **[Create](https://cloud.google.com/iap/docs/oauth-client-creation) or use an
   existing OAuth 2.0 client ID.** To use an existing OAuth 2.0 client ID,
   follow the steps in
   [How to share OAuth Clients](https://cloud.google.com/iap/docs/sharing-oauth-clients).
2. **Add the OAuth ID to the allowlist for
   [programmatic access](https://cloud.google.com/iap/docs/sharing-oauth-clients#programmatic_access)
   for the application.** Since Cloud Run is not yet a supported resource type
   in gcloud iap, you must allowlist the Client ID on the project.
3. **Create a service account.**
   [Documentation](https://cloud.google.com/iam/docs/service-accounts-create#creating),
   [Cloud Console Link](https://console.cloud.google.com/iam-admin/serviceaccounts)
4. **Add both the service account and users to the IAP Policy** in the
   "Security" tab of the Cloud Run service itself or via gcloud.
5. **Grant all users and groups** who will access the MCP Server the necessary
   permissions to
   [impersonate the service account](https://cloud.google.com/docs/authentication/use-service-account-impersonation)
   (i.e., `roles/iam.serviceAccountTokenCreator`).
6. **[Enable](https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com)
   the IAM Credentials API** for your project.