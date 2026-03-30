### Capacity errors

There may be times when the Gemini 3 Pro model is overloaded. When that happens,
Gemini CLI will ask you to decide whether you want to keep trying Gemini 3 Pro
or fallback to Gemini 2.5 Pro.

<!-- prettier-ignore -->
> [!NOTE]
> The **Keep trying** option uses exponential backoff, in which Gemini
> CLI waits longer between each retry, when the system is busy. If the retry
> doesn't happen immediately, please wait a few minutes for the request to
> process.