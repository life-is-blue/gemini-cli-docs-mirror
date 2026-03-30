### Scenario: Bulk documentation generator

You have a folder of Python scripts and want to generate a `README.md` for each
one.

1.  Save the following code as `generate_docs.sh` (or `generate_docs.ps1` for
    Windows):

    **macOS/Linux (`generate_docs.sh`)**

    ```bash
    #!/bin/bash

    # Loop through all Python files
    for file in *.py; do
      echo "Generating docs for $file..."

      # Ask Gemini CLI to generate the documentation and print it to stdout
      gemini -p "Generate a Markdown documentation summary for @$file. Print the
      result to standard output." > "${file%.py}.md"
    done
    ```

    **Windows PowerShell (`generate_docs.ps1`)**

    ```powershell
    # Loop through all Python files
    Get-ChildItem -Filter *.py | ForEach-Object {
      Write-Host "Generating docs for $($_.Name)..."

      $newName = $_.Name -replace '\.py$', '.md'
      # Ask Gemini CLI to generate the documentation and print it to stdout
      gemini -p "Generate a Markdown documentation summary for @$($_.Name). Print the result to standard output." | Out-File -FilePath $newName -Encoding utf8
    }
    ```

2.  Make the script executable and run it in your directory:

    **macOS/Linux**

    ```bash
    chmod +x generate_docs.sh
    ./generate_docs.sh
    ```

    **Windows (PowerShell)**

    ```powershell
    .\generate_docs.ps1
    ```

    This creates a corresponding Markdown file for every Python file in the
    folder.