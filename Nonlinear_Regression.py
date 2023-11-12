---
layout: default
title: About
nav_exclude: false
nav_order: 12
child_nav_order: reversed
---

# Nonlinear Regression Script

## Overview

This Python script is designed to perform nonlinear regression on a dataset. It allows users to conduct polynomial regression by specifying the degree of the polynomial. The user can choose specific columns for the regression analysis or use all numeric columns, excluding any 'DATE' column. The script outputs the model's coefficients and the R² score.

## Functionality

The script reads data from a provided CSV or Excel file, creates polynomial features based on the specified degree, and applies polynomial regression to either specific columns or all numeric columns.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a CSV or Excel format.
- `columns` (str or list of str): Specifies the columns for which the regression is to be conducted. If set to 'all', the script performs regression on all numeric columns, excluding any 'DATE' column.
- `degree` (int): The degree of the polynomial used in the regression.

### Nonlinear Regression Process

- Polynomial features are created from the selected columns based on the specified degree.
- The data is then split into training and testing sets.
- A polynomial regression model is fitted to the training data.
- The script outputs the coefficients of the model and the R² score for model evaluation.

### Exclusion of 'DATE' Column

- The script automatically detects and excludes a column named 'DATE' from the regression to preserve its original values.

## Usage

To use the script, run the following command in the terminal:

```bash
python nonlinear_regression.py <path_to_data_file> <columns/all> <degree>
```

For example, to perform polynomial regression on specific columns in a CSV file with a polynomial degree of 2:

```bash
python nonlinear_regression.py data.csv 'column1,column2,column3' 2
```

To perform polynomial regression on all numeric columns in an Excel file with a polynomial degree of 3:

```bash
python nonlinear_regression.py data.xlsx all 3
```

## Dependencies

- pandas: For data manipulation and reading files.
- scikit-learn: For conducting regression analysis and creating polynomial features.

Ensure these libraries are installed before running the script:

```bash
pip install pandas scikit-learn
```

## Notes

- The script is designed to work with datasets where the date information is stored in a column named 'DATE'.
- It automatically excludes the 'DATE' column from the regression analysis.
- The output includes the coefficients of the polynomial regression model and the R² score.

