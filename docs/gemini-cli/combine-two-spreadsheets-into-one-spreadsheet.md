### Combine two spreadsheets into one spreadsheet

Gemini CLI can process and transform data across multiple files. Use this
capability to merge reports or reformat data sets without manual copying.

Scenario: You have two .csv files: `Revenue - 2023.csv` and
`Revenue - 2024.csv`. Each file contains monthly revenue figures.

Give Gemini CLI the following prompt:

```cli
Combine the two .csv files into a single .csv file, with each year a different column.
```

Result: Gemini CLI reads each file and then asks for permission to write a new
file. Provide your permission and Gemini CLI provides the combined data:

```csv
Month,2023,2024
January,0,1000
February,0,1200
March,0,2400
April,900,500
May,1000,800
June,1000,900
July,1200,1000
August,1800,400
September,2000,2000
October,2400,3400
November,3400,1800
December,2100,9000
```