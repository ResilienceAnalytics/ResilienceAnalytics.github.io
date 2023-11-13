---
layout: default
title: Merge On Date
nav_exclude: false
nav_order: 5
child_nav_order: reversed
parent: Data Preparation
grand_parent: SATools
---

# Data Cleaner Script

## Overview

This Python script provides a solution for handling missing values within a dataset. It offers various strategies like deleting rows with missing values or imputing them using statistical methods such as mean, median, or mode. There is also a hybrid method that applies all strategies and outputs multiple files.

## Features

- Easy to use interactive CLI (Command Line Interface).
- Supports `.csv`, `.xlsx`, and `.ods` file formats for input data.
- Offers four single imputation methods and one hybrid method for flexibility.
- Saves cleaned data in the current directory or a specified path.

## How to Use

Run the script in your terminal, and you will be prompted to enter the path to your data file. After loading the data, choose one of the five options provided for handling missing values.

```bash
python data_cleaner.py
```

Follow the on-screen instructions to provide the required inputs.

## Options for Handling Missing Values

1. **Delete Rows With Missing Values**: Removes all rows that have any missing data.
2. **Impute Missing Values With Mean**: Replaces missing values with the mean of the respective column.
3. **Impute Missing Values With Median**: Replaces missing values with the median of the respective column.
4. **Impute Missing Values With Mode**: Replaces missing values with the mode of the respective column.
5. **Hybrid Method With Multiple Output Files**: Applies all the above methods and saves each result in a separate file.

## Saving the Cleaned Data

After the cleaning process, you have the option to save the cleaned data. If you choose to save, you will be asked to enter the output directory path. If you want to save in the current working directory, simply enter `.` when prompted.

## Output Files

- `cleaned_data_delete.csv`: Contains the data after rows with missing values have been removed.
- `cleaned_data_impute_mean.csv`: Contains the data after missing values have been replaced with column means.
- `cleaned_data_impute_median.csv`: Contains the data after missing values have been replaced with column medians.
- `cleaned_data_impute_mode.csv`: Contains the data after missing values have been replaced with column modes.
- Hybrid method output: For each imputation strategy, a corresponding `.csv` file is generated.

## Dependencies

- pandas: For data manipulation and reading files.
- numpy: For numerical operations.
- scikit-learn: For the `SimpleImputer` class used in imputing missing values.

Install these dependencies using pip:

```bash
pip install pandas numpy scikit-learn
```

## Notes

Ensure that the input data file is correctly formatted and that all placeholders for missing values are consistent. The script can handle numeric columns and will ignore date columns during the imputation process.
