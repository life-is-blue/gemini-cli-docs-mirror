# [Ignoring files](http://geminicli.com/docs/cli/gemini-ignore.md)


This document provides an overview of the Gemini Ignore (`.geminiignore`)
feature of the Gemini CLI.

The Gemini CLI includes the ability to automatically ignore files, similar to
`.gitignore` (used by Git) and `.aiexclude` (used by Gemini Code Assist). Adding
paths to your `.geminiignore` file will exclude them from tools that support
this feature, although they will still be visible to other services (such as
Git).