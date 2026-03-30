### Restricting logins to corporate domains

For enterprises using Google Workspace, you can enforce that users only
authenticate with their corporate Google accounts. This is a network-level
control that is configured on a proxy server, not within Gemini CLI itself. It
works by intercepting authentication requests to Google and adding a special
HTTP header.

This policy prevents users from logging in with personal Gmail accounts or other
non-corporate Google accounts.

For detailed instructions, see the Google Workspace Admin Help article on
[blocking access to consumer accounts](https://support.google.com/a/answer/1668854?hl=en#zippy=%2Cstep-choose-a-web-proxy-server%2Cstep-configure-the-network-to-block-certain-accounts).

The general steps are as follows:

1.  **Intercept Requests**: Configure your web proxy to intercept all requests
    to `google.com`.
2.  **Add HTTP Header**: For each intercepted request, add the
    `X-GoogApps-Allowed-Domains` HTTP header.
3.  **Specify Domains**: The value of the header should be a comma-separated
    list of your approved Google Workspace domain names.

**Example header:**

```
X-GoogApps-Allowed-Domains: my-corporate-domain.com, secondary-domain.com
```

When this header is present, Google's authentication service will only allow
logins from accounts belonging to the specified domains.