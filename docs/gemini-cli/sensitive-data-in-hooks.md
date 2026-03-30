### Sensitive data in hooks

If your hooks process sensitive data:

1. **Minimize logging:** Don't write sensitive data to log files.
2. **Sanitize outputs:** Remove sensitive data before outputting JSON or writing
   to stderr.