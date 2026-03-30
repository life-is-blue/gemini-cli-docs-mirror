## Release through GitHub Releases

Distributing extensions through
[GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
provides a faster installation experience by avoiding a repository clone.

Gemini CLI checks for updates by looking for the **Latest** release on GitHub.
Users can also install specific versions using the `--ref` argument with a
release tag. Use the `--pre-release` flag to install the latest version even if
it isn't marked as **Latest**.