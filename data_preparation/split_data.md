---
layout: default
title: Split Data by Date Range
nav_exclude: true
nav_order: 4
child_nav_order: reversed
parent: Data Preparation
grand_parent: SATools
---

# Split Data by Date Range Script

## Overview

This Python script is designed to filter and split a dataset based on a specified date range. It allows users to select a subset of data from a larger dataset by specifying a start date and an end date, and optionally selecting specific columns to include.

## Functionality

The script can process files in CSV, XLSX, or ODS format. It filters rows based on the 'DATE' column, ensuring that only data within the given date range is selected.

### Parameters

- `file_path` (str): The path to the data file. Supported formats include CSV, XLSX, and ODS.
- `start_date` (str): The start date for the range, in 'YYYY-MM-DD' format.
- `end_date` (str): The end date for the range, in 'YYYY-MM-DD' format.
- `columns` (list or str): The columns to include in the output. Specify 'all' to include all columns or provide a comma-separated list of column names.

### Usage

To use the script, run the following command in the terminal:

```bash
python split_data.py <path_to_data_file> <start_date> <end_date> [<columns>/all]
```

### Examples

- To filter a CSV file for data from January 1, 2022, to December 31, 2022, and include all columns:

  ```bash
  python split_data.py data.csv 2022-01-01 2022-12-31 all
  ```

- To filter an XLSX file for data from January 1, 2022, to June 30, 2022, and include only specific columns (e.g., 'Column1', 'Column2'):

  ```bash
  python split_data.py data.xlsx 2022-01-01 2022-06-30 Column1,Column2
  ```

## Dependencies

- pandas: A powerful data analysis and manipulation library for Python. Install using `pip install pandas`.
- For ODS file support, `odfpy` is required. Install using `pip install odfpy`.

## Notes

- Ensure the 'DATE' column is present in the data file and formatted correctly as dates.
- The output file will be named `filtered_<original_filename>` and saved in the same format as the input file.
- The script will not work if the 'DATE' column is missing or if the date range is invalid (e.g., start date is after the end date).
- Make sure the terminal or command prompt has sufficient permissions to read and write files in the specified directory.

