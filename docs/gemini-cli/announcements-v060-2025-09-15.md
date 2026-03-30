## Announcements: v0.6.0 - 2025-09-15

- 🎉 **Higher limits for Google AI Pro and Ultra subscribers:** We’re psyched to
  finally announce that Google AI Pro and AI Ultra subscribers now get access to
  significantly higher 2.5 quota limits for Gemini CLI!
  - **Announcement:**
    [https://blog.google/technology/developers/gemini-cli-code-assist-higher-limits/](https://blog.google/technology/developers/gemini-cli-code-assist-higher-limits/)
- 🎉**Gemini CLI Databases and BigQuery Extensions:** Connect Gemini CLI to all
  of your cloud data with Gemini CLI.
  - Announcement and how to get started with each of the below extensions:
    [https://cloud.google.com/blog/products/databases/gemini-cli-extensions-for-google-data-cloud?e=48754805](https://cloud.google.com/blog/products/databases/gemini-cli-extensions-for-google-data-cloud?e=48754805)
  - **AlloyDB:** Interact, manage and observe AlloyDB for PostgreSQL databases
    ([manage](https://github.com/gemini-cli-extensions/alloydb#configuration),
    [observe](https://github.com/gemini-cli-extensions/alloydb-observability#configuration))
  - **BigQuery:** Connect and query your BigQuery datasets or utilize a
    sub-agent for contextual insights
    ([query](https://github.com/gemini-cli-extensions/bigquery-data-analytics#configuration),
    [sub-agent](https://github.com/gemini-cli-extensions/bigquery-conversational-analytics))
  - **Cloud SQL:** Interact, manage and observe Cloud SQL for PostgreSQL
    ([manage](https://github.com/gemini-cli-extensions/cloud-sql-postgresql#configuration),[ observe](https://github.com/gemini-cli-extensions/cloud-sql-postgresql-observability#configuration)),
    Cloud SQL for MySQL
    ([manage](https://github.com/gemini-cli-extensions/cloud-sql-mysql#configuration),[ observe](https://github.com/gemini-cli-extensions/cloud-sql-mysql-observability#configuration))
    and Cloud SQL for SQL Server
    ([manage](https://github.com/gemini-cli-extensions/cloud-sql-sqlserver#configuration),[ observe](https://github.com/gemini-cli-extensions/cloud-sql-sqlserver-observability#configuration))
    databases.
  - **Dataplex:** Discover, manage, and govern data and AI artifacts
    ([extension](https://github.com/gemini-cli-extensions/dataplex#configuration))
  - **Firestore:** Interact with Firestore databases, collections and documents
    ([extension](https://github.com/gemini-cli-extensions/firestore-native#configuration))
  - **Looker:** Query data, run Looks and create dashboards
    ([extension](https://github.com/gemini-cli-extensions/looker#configuration))
  - **MySQL:** Interact with MySQL databases
    ([extension](https://github.com/gemini-cli-extensions/mysql#configuration))
  - **Postgres:** Interact with PostgreSQL databases
    ([extension](https://github.com/gemini-cli-extensions/postgres#configuration))
  - **Spanner:** Interact with Spanner databases
    ([extension](https://github.com/gemini-cli-extensions/spanner#configuration))
  - **SQL Server:** Interact with SQL Server databases
    ([extension](https://github.com/gemini-cli-extensions/sql-server#configuration))
  - **MCP Toolbox:** Configure and load custom tools for more than 30+ data
    sources
    ([extension](https://github.com/gemini-cli-extensions/mcp-toolbox#configuration))
- **JSON output mode:** Have Gemini CLI output JSON with `--output-format json`
  when invoked headlessly for easy parsing and post-processing. Includes
  response, stats and errors.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/8119) by
  [@jerop](https://github.com/jerop))
- **Keybinding triggered approvals:** When you use shortcuts (`shift+y` or
  `shift+tab`) to activate YOLO/auto-edit modes any pending confirmation dialogs
  will now approve. ([pr](https://github.com/google-gemini/gemini-cli/pull/6665)
  by [@bulkypanda](https://github.com/bulkypanda))
- **Chat sharing:** Convert the current conversation to a Markdown or JSON file
  with _/chat share &lt;file.md|file.json>_
  ([pr](https://github.com/google-gemini/gemini-cli/pull/8139) by
  [@rramkumar1](https://github.com/rramkumar1))
- **Prompt search:** Search your prompt history using `ctrl+r`.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/5539) by
  [@Aisha630](https://github.com/Aisha630))
- **Input undo/redo:** Recover accidentally deleted text in the input prompt
  using `ctrl+z` (undo) and `ctrl+shift+z` (redo).
  ([pr](https://github.com/google-gemini/gemini-cli/pull/4625) by
  [@masiafrest](https://github.com/masiafrest))
- **Loop detection confirmation:** When loops are detected you are now presented
  with a dialog to disable detection for the current session.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/8231) by
  [@SandyTao520](https://github.com/SandyTao520))
- **Direct to Google Cloud Telemetry:** Directly send telemetry to Google Cloud
  for a simpler and more streamlined setup.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/8541) by
  [@jerop](https://github.com/jerop))
- **Visual Mode Indicator Revamp:** ‘shell’, 'accept edits' and 'yolo' modes now
  have colors to match their impact / usage. Input box now also updates.
  ([shell](https://imgur.com/a/DovpVF1),
  [accept-edits](https://imgur.com/a/33KDz3J),
  [yolo](https://imgur.com/a/tbFwIWp),
  [pr](https://github.com/google-gemini/gemini-cli/pull/8200) by
  [@miguelsolorio](https://github.com/miguelsolorio))
- **Small features, polish, reliability & bug fixes:** A large amount of
  changes, smaller features, UI updates, reliability and bug fixes + general
  polish made it in this week!