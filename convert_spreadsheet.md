---
layout: default
title: convert Spreadsheet
nav_exclude: false
nav_order: 1
child_nav_order: reversed
parent : Miscellaneous
grand_parent : SATools
---
# Spreadsheet Conversion Script

## Overview

This Python script facilitates the conversion of spreadsheet files between different formats, such as XLSX, CSV, and ODS. Users can specify the input file, the desired output file, and the format for the output file, making it a versatile tool for handling various spreadsheet formats.

## Functionality

The script reads an input spreadsheet file and converts it to a specified format. It supports conversion to and from the most commonly used spreadsheet formats.

### Parameters

- `input_file_path` (str): Path to the input file, which can be in formats like XLSX, CSV, or ODS.
- `output_file_path` (str): Path for saving the converted file.
- `output_format` (str): Desired output file format. Options include 'xlsx', 'csv', and 'ods'.

### Supported File Formats

- **Input Formats**: XLSX, ODS (and potentially others supported by `pandas`).
- **Output Formats**: XLSX, CSV, ODS.

## Usage

To use the script, run the following command in the terminal:

```bash
python convert_spreadsheet.py <input_file_path> <output_file_path> <output_format>
```

Examples:
- To convert an ODS file to XLSX format:
  ```bash
  python convert_spreadsheet.py data.ods data_converted.xlsx xlsx
  ```
- To convert an XLSX file to CSV format:
  ```bash
  python convert_spreadsheet.py data.xlsx data_converted.csv csv
  ```

## Dependencies

- pandas: For data manipulation and reading files. Install using `pip install pandas`.
- For ODS support, `odfpy` might be required. Install using `pip install odfpy`.

## Notes

- The script uses `pandas` to read and write data, offering robust support for handling various data types within spreadsheets.
- The format conversion process is straightforward and user-friendly, requiring minimal inputs from the user.
- Users should ensure that the input and output file paths and formats are correctly specified to avoid errors during conversion.

