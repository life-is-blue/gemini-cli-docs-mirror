### Optimize JSON parsing

For large inputs (like `AfterModel` receiving a large context), standard JSON
parsing can be slow. If you only need one field, consider streaming parsers or
lightweight extraction logic, though for most shell scripts `jq` is sufficient.