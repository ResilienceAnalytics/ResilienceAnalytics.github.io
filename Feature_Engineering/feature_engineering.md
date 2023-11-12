---layout: default
title: Feature Engineering
nav_exclude: false
nav_order: 1
child_nav_order: reversed
parent : feature_engineering
grand_parent : SATools
---

# Feature Engineering Script

## Overview

This Python script is designed for feature engineering, a process of creating new derived variables (features) from existing data. Feature engineering can significantly enhance machine learning models by introducing additional information and insights, potentially improving model performance and accuracy.

## Functionality

The script reads data from a provided CSV or Excel file and allows users to define and create new features based on existing data columns through specified mathematical or logical expressions.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a CSV or Excel format.
- `new_features` (dict): A dictionary where keys are new column names and values are expressions to generate these columns.

### Feature Engineering Process

- Users can create new features by specifying expressions that combine, transform, or compute new values from existing data columns.
- The script dynamically evaluates these expressions to generate new columns in the dataset.

## Usage

To use the script, run the following command in the terminal:

```bash
python feature_engineering.py <path_to_data_file> <new_features_dictionary>
```

For example, to create a new feature that is the product of two existing columns in a CSV file:

```bash
python feature_engineering.py data.csv "{'new_feature': 'data[\'column1\'] * data[\'column2\']'}"
```

### Caution with `eval`

- This script uses the `eval` function to dynamically execute the expressions defined in the `new_features` dictionary.
- While `eval` provides flexibility, it should be used cautiously as it can execute arbitrary code. Ensure that the input expressions are safe and do not contain harmful code.

## Dependencies

- pandas: For data manipulation and reading files.

Ensure pandas is installed before running the script:

```bash
pip install pandas
```

## Notes

- Feature engineering is a creative and crucial step in the data science workflow. It involves domain knowledge to create meaningful features that can capture essential aspects of the problem.
- The script is flexible, allowing users to define a wide range of transformations and interactions between variables.
- The output includes the original data with the newly engineered features, ready for further analysis or model training.
