### Forking

If you are forking the repository you will be able to run the Build, Test and
Integration test workflows. However in order to make the integration tests run
you'll need to add a
[GitHub Repository Secret](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)
with a value of `GEMINI_API_KEY` and set that to a valid API key that you have
available. Your key and secret are private to your repo; no one without access
can see your key and you cannot see any secrets related to this repo.

Additionally you will need to click on the `Actions` tab and enable workflows
for your repository, you'll find it's the large blue button in the center of the
screen.