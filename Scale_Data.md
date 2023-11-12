---
layout: default
title: Scale Data
nav_exclude: false
nav_order: 1
child_nav_order: reversed
parent : Data_Preparation
grand_parent : SATools
---

# Data Scaling Script

## Overview

This Python script provides functionality for scaling data within a specified file. It supports normalization, standardization, and Z-score scaling methods. Users can select specific columns for scaling or apply scaling to all numeric columns, excluding a designated 'DATE' column.

## Functionality

The script reads data from a provided file path, which can be in CSV or Excel format. It then applies the chosen scaling method to either specific columns or all numeric columns, while automatically excluding any 'DATE' column from scaling.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a CSV or Excel format.
- `method` (str): The scaling method to be used. Options are 'normalization', 'standardization', and 'z-score'.
- `columns` (str or list of str): Specifies the columns to be scaled. If set to 'all', all numeric columns except 'DATE' are scaled. If specific columns are to be scaled, they should be provided as a comma-separated string.

### Scaling Methods

- **Normalization**: Scales the data to a range of 0 to 1.
- **Standardization**: Scales the data to have a mean of 0 and a standard deviation of 1.
- **Z-score**: Similar to standardization, transforms the data to z-scores.

### Exclusion of 'DATE' Column

The script automatically detects and excludes a column named 'DATE' from scaling to preserve its original values.

## Usage

To use the script, run the following command in the terminal:

```bash
python scale_data.py <path_to_data_file> <method> <columns/all>
```

For example, to apply normalization to specific columns in a CSV file:

```bash
python scale_data.py data.csv normalization 'column1,column2'
```

To apply standardization to all numeric columns in an Excel file:

```bash
python scale_data.py data.xlsx standardization all
```

## Dependencies

- pandas: For data manipulation and reading files.
- scikit-learn: For applying scaling methods.

Ensure these libraries are installed before running the script:

```bash
pip install pandas scikit-learn
```

## Notes

- The script assumes the presence of a 'DATE' column in the dataset.
- It is compatible with various file formats that pandas can read.
- The scaled data is printed as output in the terminal.

