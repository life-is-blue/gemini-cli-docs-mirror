## Authentication or login errors

- **Error:
  `You must be a named user on your organization's Gemini Code Assist Standard edition subscription to use this service. Please contact your administrator to request an entitlement to Gemini Code Assist Standard edition.`**
  - **Cause:** This error might occur if Gemini CLI detects the
    `GOOGLE_CLOUD_PROJECT` or `GOOGLE_CLOUD_PROJECT_ID` environment variable is
    defined. Setting these variables forces an organization subscription check.
    This might be an issue if you are using an individual Google account not
    linked to an organizational subscription.

  - **Solution:**
    - **Individual Users:** Unset the `GOOGLE_CLOUD_PROJECT` and
      `GOOGLE_CLOUD_PROJECT_ID` environment variables. Check and remove these
      variables from your shell configuration files (for example, `.bashrc`,
      `.zshrc`) and any `.env` files. If this doesn't resolve the issue, try
      using a different Google account.

    - **Organizational Users:** Contact your Google Cloud administrator to be
      added to your organization's Gemini Code Assist subscription.

- **Error:
  `Failed to sign in. Message: Your current account is not eligible... because it is not currently available in your location.`**
  - **Cause:** Gemini CLI does not currently support your location. For a full
    list of supported locations, see the following pages:
    - Gemini Code Assist for individuals:
      [Available locations](https://developers.google.com/gemini-code-assist/resources/available-locations#americas)

- **Error: `Failed to sign in. Message: Request contains an invalid argument`**
  - **Cause:** Users with Google Workspace accounts or Google Cloud accounts
    associated with their Gmail accounts may not be able to activate the free
    tier of the Google Code Assist plan.
  - **Solution:** For Google Cloud accounts, you can work around this by setting
    `GOOGLE_CLOUD_PROJECT` to your project ID. Alternatively, you can obtain the
    Gemini API key from
    [Google AI Studio](http://aistudio.google.com/app/apikey), which also
    includes a separate free tier.

- **Error: `UNABLE_TO_GET_ISSUER_CERT_LOCALLY` or
  `unable to get local issuer certificate`**
  - **Cause:** You may be on a corporate network with a firewall that intercepts
    and inspects SSL/TLS traffic. This often requires a custom root CA
    certificate to be trusted by Node.js.
  - **Solution:** First try setting `NODE_USE_SYSTEM_CA`; if that does not
    resolve the issue, set `NODE_EXTRA_CA_CERTS`.
    - Set the `NODE_USE_SYSTEM_CA=1` environment variable to tell Node.js to use
      the operating system's native certificate store (where corporate
      certificates are typically already installed).
      - Example: `export NODE_USE_SYSTEM_CA=1` (Windows PowerShell:
        `$env:NODE_USE_SYSTEM_CA=1`)
    - Set the `NODE_EXTRA_CA_CERTS` environment variable to the absolute path of
      your corporate root CA certificate file.
      - Example: `export NODE_EXTRA_CA_CERTS=/path/to/your/corporate-ca.crt`
        (Windows PowerShell:
        `$env:NODE_EXTRA_CA_CERTS="C:\path\to\your\corporate-ca.crt"`)