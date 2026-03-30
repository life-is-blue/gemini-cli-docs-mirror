# [Gemini CLI for the enterprise](http://geminicli.com/docs/cli/enterprise.md)


This document outlines configuration patterns and best practices for deploying
and managing Gemini CLI in an enterprise environment. By leveraging system-level
settings, administrators can enforce security policies, manage tool access, and
ensure a consistent experience for all users.

<!-- prettier-ignore -->
> [!WARNING]
> The patterns described in this document are intended to help
> administrators create a more controlled and secure environment for using
> Gemini CLI. However, they should not be considered a foolproof security
> boundary. A determined user with sufficient privileges on their local machine
> may still be able to circumvent these configurations. These measures are
> designed to prevent accidental misuse and enforce corporate policy in a
> managed environment, not to defend against a malicious actor with local
> administrative rights.