---
layout: default
title: Convert Spreadsheet Folder
nav_exclude: false
nav_order: 3
child_nav_order: reversed
parent: Data Preparation
grand_parent: SATools
---


# Merge Files on Date Script

## Overview

This Python script is designed to automate the merging of multiple ODS spreadsheet files within a specified directory, based on a common 'DATE' column. The merged data is then saved into a single output file, facilitating data consolidation for time-series analysis or reporting.

## Functionality

The script identifies all ODS files in a given input directory, merges them into a single DataFrame by aligning rows based on the 'DATE' column, and then outputs the merged data to a specified file.

### Parameters

- `input_dir` (str): The path to the directory containing the ODS files to be merged.
- `output_file_path` (str): The file path where the merged data will be saved.

### Usage

To use the script, run the following command in the terminal:

```bash
python merge_files_on_date.py <path_to_input_directory> <path_to_output_file>
```

### Examples

- Merging all ODS files in a directory and saving the combined data as an Excel file:

  ```bash
  python merge_files_on_date.py /path/to/input/directory combined_data.xlsx
  ```

## Dependencies

- pandas: A powerful data analysis and manipulation library for Python. Install using `pip install pandas`.
- odfpy: An ODS file support library for Python. Install using `pip install odfpy`.

## Notes

- The script currently only supports ODS files as input. Ensure that the input directory does not contain any non-ODS files.
- It's important that all ODS files in the directory have a 'DATE' column in a consistent format, as this is used as the key for merging.
- The output file will be saved in the Excel format due to the current limitations of the `pandas` library's support for the ODS format.

