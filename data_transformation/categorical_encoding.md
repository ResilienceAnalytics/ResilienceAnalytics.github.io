---
layout: default
title: Categorical Encoding
nav_exclude: false
nav_order: 1
hild_nav_order: reversed
parent: Data Transformation
grand_parent: SATools
---

# Categorical Encoding Script

## Overview

This Python script is designed to perform categorical encoding on a dataset. It allows users to apply either one-hot encoding or label encoding to specific columns or all categorical columns in the dataset. This transformation is essential for converting categorical data into a format that can be easily used by machine learning algorithms.

## Functionality

The script reads data from a provided CSV or Excel file and applies the chosen encoding method to the selected categorical columns.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a CSV or Excel format.
- `columns` (str or list of str): Specifies the columns to which the encoding is to be applied. If set to 'all', the script performs encoding on all categorical columns.
- `encoding_type` (str): Type of encoding to be used. Options are 'onehot' or 'label'.

### Types of Encoding

- **One-Hot Encoding**: 
  - Each unique category value is transformed into a new column with a binary value (1 or 0).
  - Useful when the categorical variable does not have an inherent order.
  - Implemented using `OneHotEncoder` from scikit-learn.

- **Label Encoding**:
  - Each unique category value is assigned an integer value.
  - More memory-efficient than one-hot encoding.
  - Suitable for ordinal categorical variables where the order matters.
  - Implemented using `LabelEncoder` from scikit-learn.

## Usage

To use the script, run the following command in the terminal:

```bash
python categorical_encoding.py <path_to_data_file> <columns/all> <encoding_type>
```

For example, to apply one-hot encoding to specific columns in a CSV file:

```bash
python categorical_encoding.py data.csv 'column1,column2' onehot
```

To apply label encoding to all categorical columns in an Excel file:

```bash
python categorical_encoding.py data.xlsx all label
```

## Dependencies

- pandas: For data manipulation and reading files.
- scikit-learn: For performing the encoding transformations.

Ensure these libraries are installed before running the script:

```bash
pip install pandas scikit-learn
```

## Notes

- The script is designed to handle datasets with various types of categorical data.
- It automatically applies the specified encoding to the chosen columns.
- The output includes the data with encoded categorical values, ready for further analysis or model training.

---

This documentation provides a comprehensive guide to using the Categorical Encoding Script, detailing its functionality, usage, and requirements.
