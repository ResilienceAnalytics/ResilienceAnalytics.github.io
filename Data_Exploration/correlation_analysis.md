---
layout: default
title: Correlation Cnalysis
nav_exclude: false
nav_order: 13
child_nav_order: reversed
parent : Data_Exploration
grand_parent : SATools
---

# Correlation Analysis Script

## Overview

This Python script is designed for performing correlation analysis on a dataset provided by the user. The script calculates the correlation matrix for specified columns or all numeric columns, automatically excluding any 'DATE' column present in the dataset.

## Functionality

The script reads data from a CSV or Excel file and computes the Pearson correlation coefficient between the specified columns.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a CSV or Excel format.
- `columns` (str or list of str): Specifies the columns for which the correlation analysis is to be conducted. If set to 'all', the script computes correlations for all numeric columns, excluding any 'DATE' column.

### Correlation Method

- The script uses the Pearson correlation coefficient method by default to measure the strength and direction of the linear relationship between pairs of variables.

### Exclusion of 'DATE' Column

- The script automatically detects and excludes a column named 'DATE' from the correlation analysis to preserve its original values.

## Usage

To use the script, run the following command in the terminal:

```bash
python correlation_analysis.py <path_to_data_file> <columns/all>
```

For example, to compute the correlation matrix for specific columns in a CSV file:

```bash
python correlation_analysis.py data.csv 'column1,column2'
```

To compute the correlation matrix for all numeric columns in an Excel file:

```bash
python correlation_analysis.py data.xlsx all
```

## Dependencies

- pandas: For data manipulation and reading files.

Ensure pandas is installed before running the script:

```bash
pip install pandas
```

## Notes

- The script is designed to work with datasets where the date information is stored in a column named 'DATE'.
- It automatically excludes the 'DATE' column from the correlation analysis.
- The correlation matrix is printed as output in the terminal.
