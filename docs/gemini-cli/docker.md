### Docker

We also run a Google cloud build called
[release-docker.yml](https://github.com/google-gemini/gemini-cli/blob/main/.gcp/release-docker.yml). Which publishes the sandbox
docker to match your release. This will also be moved to GH and combined with
the main release file once service account permissions are sorted out.