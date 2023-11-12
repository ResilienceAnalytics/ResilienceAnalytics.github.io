---
layout: default
title: Statistical Analysis Tools
nav_exclude: false
nav_order: 3
has_children: true
child_nav_order: reversed
parent: Miscellaneous
grand_parent: SAT Tools
---

# Box-Cox and Yeo-Johnson Transformation Script

## Overview

This Python script is designed to perform Box-Cox or Yeo-Johnson transformations on a dataset. These transformations are utilized to stabilize variance, make the data more normal distribution-like, and are particularly useful for handling skewed data. The script allows users to apply the transformation to specific columns or to all numeric columns in the dataset.

## Functionality

The script reads data from a provided CSV or Excel file and applies the chosen transformation method to the selected numeric columns.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a CSV or Excel format.
- `columns` (str or list of str): Specifies the columns to which the transformation is to be applied. If set to 'all', the script performs the transformation on all numeric columns.
- `method` (str): Type of transformation to be used. Options are 'boxcox' or 'yeojohnson'.

### Types of Transformations

- **Box-Cox Transformation**:
  - A family of power transformations that are defined for strictly positive numbers.
  - It's particularly effective in handling right-skewed data.
  - The script adds an offset of 1 to accommodate non-positive values.

- **Yeo-Johnson Transformation**:
  - A modification of the Box-Cox transformation that extends its applicability to non-positive values.
  - It's useful for a wider range of data, including zero and negative values.

Both transformations aim to make the data more normally distributed or to stabilize variance across different levels of input variables.

## Usage

To use the script, run the following command in the terminal:

```bash
python transform_data.py <path_to_data_file> <columns/all> <method>
```

For example, to apply a Box-Cox transformation to specific columns in a CSV file:

```bash
python transform_data.py data.csv 'column1,column2' boxcox
```

To apply a Yeo-Johnson transformation to all numeric columns in an Excel file:

```bash
python transform_data.py data.xlsx all yeojohnson
```

## Dependencies

- pandas: For data manipulation and reading files.
- scipy and sklearn: For performing the transformations.

Ensure these libraries are installed before running the script:

```bash
pip install pandas scipy scikit-learn
```

## Notes

- The script is designed to handle datasets with various types of numerical data.
- The chosen transformation is applied to the specified columns, and the script outputs the data with transformed values.
- The use of these transformations can be crucial for models that assume normally distributed residuals.

