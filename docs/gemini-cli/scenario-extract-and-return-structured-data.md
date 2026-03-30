### Scenario: Extract and return structured data

1.  Save the following script as `generate_json.sh` (or `generate_json.ps1` for
    Windows):

    **macOS/Linux (`generate_json.sh`)**

    ```bash
    #!/bin/bash

    # Ensure we are in a project root
    if [ ! -f "package.json" ]; then
      echo "Error: package.json not found."
      exit 1
    fi

    # Extract data
    gemini --output-format json "Return a raw JSON object with keys 'version' and 'deps' from @package.json" | jq -r '.response' > data.json
    ```

    **Windows PowerShell (`generate_json.ps1`)**

    ```powershell
    # Ensure we are in a project root
    if (-not (Test-Path "package.json")) {
      Write-Error "Error: package.json not found."
      exit 1
    }

    # Extract data (requires jq installed, or you can use ConvertFrom-Json)
    $output = gemini --output-format json "Return a raw JSON object with keys 'version' and 'deps' from @package.json" | ConvertFrom-Json
    $output.response | Out-File -FilePath data.json -Encoding utf8
    ```

2.  Run the script:

    **macOS/Linux**

    ```bash
    chmod +x generate_json.sh
    ./generate_json.sh
    ```

    **Windows (PowerShell)**

    ```powershell
    .\generate_json.ps1
    ```

3.  Check `data.json`. The file should look like this:

    ```json
    {
      "version": "1.0.0",
      "deps": {
        "react": "^18.2.0"
      }
    }
    ```