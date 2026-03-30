## Extract structured JSON data

When writing a script, you often need structured data (JSON) to pass to tools
like `jq`. To get pure JSON data from the model, combine the
`--output-format json` flag with `jq` to parse the response field.