---
layout: default
title: Merge On Date
nav_exclude: false
nav_order: 2
child_nav_order: reversed
parent : Data Preparation
grand_parent : SATools
---

# Documentation: Merge Files on Date

## Overview

This Python script is designed to merge multiple ODS files based on a common 'DATE' column. The merged data is then saved into a new file. The script is particularly useful for combining datasets from different sources that share a date-based structure.

## Function `merge_files_on_date`

### Purpose

Merges multiple ODS files into a single file, aligning data based on a shared 'DATE' column.

### Parameters

- `file_paths` (list of str): Paths to the ODS files to be merged. Each file should have a 'DATE' column.
- `output_file_path` (str): Path where the combined file will be saved. The output file will be in Excel format due to pandas' limitations in saving to ODS format.

### Process

1. **Reading Files**: Each file specified in `file_paths` is read into a pandas DataFrame. The 'DATE' column of each DataFrame is converted to the datetime format for consistency.
2. **Merging**: All DataFrames are concatenated into a single DataFrame based on the 'DATE' column. The data is then sorted by 'DATE'.
3. **Saving Output**: The combined DataFrame is saved to the specified `output_file_path` in Excel format.

## Command-Line Execution

### Usage

```bash
python combine.py <path_to_output_ods_file> <path_to_first_ods_file> <path_to_second_ods_file> ...
```

### Requirements

- The script requires at least two input files to be specified along with the output file path.
- All input files must be in the ODS format and contain a 'DATE' column.

### Example

```bash
python combine.py combined_data.xlsx data1.ods data2.ods data3.ods
```

This example command will merge `data1.ods`, `data2.ods`, and `data3.ods` based on their 'DATE' columns and save the output in `combined_data.xlsx`.

## Dependencies

- pandas: The script uses pandas for reading, processing, and saving data.

## Notes

- The output file is saved in Excel format (.xlsx) as pandas does not directly support saving to ODS format.
- The script assumes that all input files have a 'DATE' column in a format that can be converted to pandas datetime.

