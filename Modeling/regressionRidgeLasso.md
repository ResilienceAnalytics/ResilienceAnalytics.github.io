---
layout: default
title: Regression Ridge Lasso
nav_exclude: false
nav_order: 1
child_nav_order: reversed
parent : Modeling
grand_parent : SATools
---

# Ridge and Lasso Regression Script

## Overview

This Python script is designed to perform Ridge or Lasso regression on a dataset. The user can choose specific columns for the regression analysis or use all numeric columns, excluding any 'DATE' column. The script allows the specification of the regularization method (Ridge or Lasso) and the regularization strength (alpha).

## Functionality

The script reads data from a provided CSV or Excel file, standardizes the data, and applies the chosen regression method to either specific columns or all numeric columns.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a CSV or Excel format.
- `columns` (str or list of str): Specifies the columns for which the regression is to be conducted. If set to 'all', the script performs regression on all numeric columns, excluding any 'DATE' column.
- `method` (str): The regression method to be used. Options are 'ridge' (Ridge regression) or 'lasso' (Lasso regression).
- `alpha` (float): The regularization strength. Higher values specify stronger regularization.

### Regression Process

- The data is first standardized using `StandardScaler`.
- It is then split into training and testing sets.
- Ridge or Lasso regression is performed based on the user's choice.
- The script outputs the coefficients of the model and the R² score for model evaluation.

### Exclusion of 'DATE' Column

- The script automatically detects and excludes a column named 'DATE' from the regression to preserve its original values.

## Usage

To use the script, run the following command in the terminal:

```bash
python regression.py <path_to_data_file> <columns/all> <method> <alpha>
```

For example, to perform Ridge regression on specific columns in a CSV file with alpha set to 1.0:

```bash
python regression.py data.csv 'column1,column2,column3' ridge 1.0
```

To perform Lasso regression on all numeric columns in an Excel file with alpha set to 0.5:

```bash
python regression.py data.xlsx all lasso 0.5
```

## Dependencies

- pandas: For data manipulation and reading files.
- scikit-learn: For conducting regression analysis and data standardization.

Ensure these libraries are installed before running the script:

```bash
pip install pandas scikit-learn
```

## Notes

- The script is designed to work with datasets where the date information is stored in a column named 'DATE'.
- It automatically excludes the 'DATE' column from the regression analysis.
- The output includes the coefficients of the regression model and the R² score.

