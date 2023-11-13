---
layout: default
title: Convert Spreadsheet Folder
nav_exclude: false
nav_order: 4
child_nav_order: reversed
parent: Miscellaneous
grand_parent: SATools
---

# Spreadsheet Folder Conversion Script

## Overview

This Python script automates the conversion of multiple spreadsheet files within a directory, accommodating different formats such as XLSX, CSV, and ODS. It is designed to process all files in a specified input directory and output them in the desired format to a target directory.

## Functionality

The script scans through all spreadsheet files in the given input directory, converts each file to the specified format, and saves them to the output directory.

### Parameters

- `input_directory` (str): Path to the directory containing the input files.
- `output_directory` (str): Path to the directory where the converted files will be saved.
- `output_format` (str): The desired format for the output files. Options include 'xlsx', 'csv', and 'ods'.

### Supported File Formats

- **Input Formats**: XLSX, ODS, CSV (and potentially others supported by `pandas`).
- **Output Formats**: XLSX, CSV, ODS.

## Usage

To use the script, run the following command in the terminal:

```bash
python convert_spreadsheet_folder.py <input_directory> <output_directory> <output_format>
```

Examples:
- To convert all files in a directory from ODS to XLSX format:
  ```bash
  python convert_spreadsheet_folder.py Data_CSV/ Data_XLSX/ xlsx
  ```
- To convert all files in a directory from CSV to ODS format:
  ```bash
  python convert_spreadsheet_folder.py Data_CSV/ Data_ODS/ ods
  ```

## Dependencies

- pandas: Required for data manipulation and file reading. Install using `pip install pandas`.
- For ODS support, `odfpy` is required. Install using `pip install odfpy`.

## Notes

- The script uses `pandas` for reading and writing spreadsheet data, thus providing extensive support for various data types contained within spreadsheets.
- The batch conversion process is efficient and user-friendly, requiring only the directory paths and the desired output format.
- Users should verify that the paths to the input and output directories, as well as the output format, are correctly specified to prevent errors.
- The script includes error handling to skip files with unsupported formats and continue processing.
```

This markdown documentation provides a structured and detailed guide for using the `convert_spreadsheet_folder.py` script, including an overview, functionality description, usage examples, and notes on dependencies and error handling.
