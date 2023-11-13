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

This Python script efficiently handles missing values in datasets. It offers flexible imputation strategies including mean, median, and a hybrid method. The script supports a variety of file formats and provides an interactive CLI for ease of use.

## Features

- Interactive CLI for ease of use.
- Supports `.csv`, `.xlsx`, and `.ods` file formats.
- Multiple imputation methods: mean, median, and hybrid.
- Option to save cleaned data in a specified directory.

## How to Use

1. Run the script in your terminal:

   ```bash
   python data_cleaner.py
   ```

2. Enter the path to your data file when prompted.
3. Choose the imputation method for numerical data.
4. Decide whether to save the cleaned data.

## Imputation Options

- **Mean**: Replaces missing values with the column's mean.
- **Median**: Uses the median for missing data replacement.
- **Hybrid**: Applies both mean and median imputations, saving the results in separate files.

## Saving Options

- Press `Enter` or type `yes` to save the cleaned data.
- Specify the output directory path when prompted.
- For the hybrid method, separate files for each imputation strategy are saved in the specified directory.

## Output Files

- Named after the original file with the addition of the imputation strategy.
- For the hybrid method, two files are generated: one for mean and another for median imputation.

## Dependencies

- Pandas, Numpy, and Scikit-learn.

  Install with pip:

  ```bash
  pip install pandas numpy scikit-learn
  ```

## Notes

- Ensure the input file is well-formatted.
- The script handles numeric and categorical data but excludes datetime columns from imputation.
