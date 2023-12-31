---
layout: default
title: Principal Component Analysis
nav_exclude: false
nav_order: 3
child_nav_order: reversed
parent : Modeling
grand_parent : SATools
---

# Principal Component Analysis (PCA)

## Overview

This Python script performs Principal Component Analysis (PCA) on a dataset provided by the user. It allows users to specify particular columns for the analysis or use all numeric columns, excluding any 'DATE' column. The script outputs the principal components and the explained variance ratio.

## Functionality

The script reads data from a CSV or Excel file and conducts PCA to reduce the dimensionality of the dataset while retaining the most significant features.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a CSV or Excel format.
- `columns` (str or list of str): Specifies the columns for which the PCA is to be conducted. If set to 'all', the script performs PCA on all numeric columns, excluding any 'DATE' column.
- `n_components` (int): The number of principal components to retain in the analysis.

### PCA Process

- The data is first standardized to have a mean of zero and a standard deviation of one.
- PCA is then performed on the standardized data.
- The script outputs the principal components and the proportion of variance explained by each component.

### Exclusion of 'DATE' Column

- The script automatically detects and excludes a column named 'DATE' from the PCA to preserve its original values.

## Usage

To use the script, run the following command in the terminal:

```bash
python pca_analysis.py <path_to_data_file> <columns/all> <n_components>
```

For example, to perform PCA on specific columns in a CSV file with two principal components:

```bash
python pca_analysis.py data.csv 'column1,column2,column3' 2
```

To perform PCA on all numeric columns in an Excel file with three principal components:

```bash
python pca_analysis.py data.xlsx all 3
```

## Dependencies

- pandas: For data manipulation and reading files.
- scikit-learn: For conducting PCA and data standardization.

Ensure these libraries are installed before running the script:

```bash
pip install pandas scikit-learn
```

## Notes

- The script is designed to work with datasets where the date information is stored in a column named 'DATE'.
- It automatically excludes the 'DATE' column from the PCA.
- The output includes the principal components and the explained variance ratio.

