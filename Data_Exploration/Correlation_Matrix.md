---
layout: default
title : Correlation Matrix
nav_exclude: false
nav_order: 2
child_nav_order: reversed
parent : Data_Exploration
grand_parent : SATools
---

# Correlation Matrix Generator

## Overview

This Python script is designed to calculate and visualize the correlation matrix from a given dataset. It allows users to specify particular columns for analysis or use all numeric columns by default. The script generates a correlation matrix and a corresponding heatmap.

## Function: `generate_correlation_matrix`

### Purpose

To create a correlation matrix and heatmap from specified columns of a data file.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a format readable by pandas, such as Excel (.xlsx, .xls) or CSV.
- `columns` (list of str): A list of column names to be included in the correlation analysis. If None, the script uses all numeric columns in the dataset.

### Functionality

1. **Reading Data**: The script reads the data from the specified file path using pandas. It supports various formats like Excel and CSV.
2. **Column Selection**: If specific columns are provided, the script includes only those columns for correlation analysis.
3. **Correlation Calculation**: It calculates the correlation matrix, considering only numeric columns (`numeric_only=True`) to avoid future warnings and ensure compatibility with upcoming pandas versions.
4. **Heatmap Generation**: A heatmap is created using seaborn to visualize the correlation matrix. This heatmap is annotated and uses a 'coolwarm' color palette for better readability.
5. **Saving Outputs**: The script saves the correlation matrix as an Excel file (`correlation_matrix.xlsx`) and the heatmap as a PNG image (`correlation_heatmap.png`).

## Usage

To use the script, run the following command in the terminal:

```bash
python correlation_matrix.py <path_to_data_file> [column1 column2 ...]
```

- Provide the path to the data file as the first argument.
- Optionally, specify the columns for which you want to calculate the correlation. If no columns are specified, all numeric columns are used.

### Example

```bash
python correlation_matrix.py data.xlsx Column1 Column2
```

This command will calculate the correlation matrix for 'Column1' and 'Column2' in 'data.xlsx'.

## Dependencies

- pandas: For data manipulation and reading files.
- seaborn and matplotlib: For generating and saving the heatmap.

Ensure these libraries are installed before running the script:

```bash
pip install pandas seaborn matplotlib
```

## Notes

- The script assumes the presence of a 'DATE' column in the dataset.
- It is compatible with various file formats that pandas can read.
- The heatmap and correlation matrix files are saved in the same directory as the script.

