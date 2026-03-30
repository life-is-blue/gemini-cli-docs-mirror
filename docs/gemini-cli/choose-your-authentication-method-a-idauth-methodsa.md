## Choose your authentication method <a id="auth-methods"></a>

Select the authentication method that matches your situation in the table below:

| User Type / Scenario                                                   | Recommended Authentication Method                                | Google Cloud Project Required                               |
| :--------------------------------------------------------------------- | :--------------------------------------------------------------- | :---------------------------------------------------------- |
| Individual Google accounts                                             | [Sign in with Google](#login-google)                             | No, with exceptions                                         |
| Organization users with a company, school, or Google Workspace account | [Sign in with Google](#login-google)                             | [Yes](#set-gcp)                                             |
| AI Studio user with a Gemini API key                                   | [Use Gemini API Key](#gemini-api)                                | No                                                          |
| Google Cloud Vertex AI user                                            | [Vertex AI](#vertex-ai)                                          | [Yes](#set-gcp)                                             |
| [Headless mode](#headless)                                             | [Use Gemini API Key](#gemini-api) or<br> [Vertex AI](#vertex-ai) | No (for Gemini API Key)<br> [Yes](#set-gcp) (for Vertex AI) |