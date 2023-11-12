# Descriptive Statistical Analysis Script

## Overview

This Python script is designed to perform descriptive statistical analysis on a dataset. It allows users to obtain key statistical measures such as mean, median, standard deviation, and more for specific columns or all columns in a dataset. The script can handle data provided in CSV or Excel formats.

## Functionality

The script reads data from a provided file and computes descriptive statistics for the chosen columns.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a CSV or Excel format.
- `columns` (str or list of str): Specifies the columns for which the analysis is to be conducted. If set to 'all', the script performs analysis on all columns.

### Descriptive Statistics

- The script computes key statistics including:
  - Count: Number of non-missing values.
  - Mean: Average value.
  - Std: Standard deviation.
  - Min: Minimum value.
  - 25%, 50%, 75%: Percentiles.
  - Max: Maximum value.

## Usage

To use the script, run the following command in the terminal:

```bash
python descriptive_stats.py <path_to_data_file> <columns/all>
```

For example, to obtain descriptive statistics for specific columns in a CSV file:

```bash
python descriptive_stats.py data.csv 'column1,column2'
```

To obtain descriptive statistics for all columns in an Excel file:

```bash
python descriptive_stats.py data.xlsx all
```

## Dependencies

- pandas: For data manipulation and reading files.

Ensure pandas is installed before running the script:

```bash
pip install pandas
```

## Notes

- The script is designed to handle datasets with various types of numerical and categorical data.
- It automatically calculates and displays the descriptive statistics for the specified columns.
- The output includes a comprehensive summary of key statistical measures for each column.

