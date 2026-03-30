## Running in Google Cloud environments <a id="cloud-env"></a>

When running Gemini CLI within certain Google Cloud environments, authentication
is automatic.

In a Google Cloud Shell environment, Gemini CLI typically authenticates
automatically using your Cloud Shell credentials. In Compute Engine
environments, Gemini CLI automatically uses Application Default Credentials
(ADC) from the environment's metadata server.

If automatic authentication fails, use one of the interactive methods described
on this page.