---
layout: default
title: Data Grouping and Averaging Script
nav_exclude: false
nav_order: 7
child_nav_order: reversed
parent: Data Transformation
grand_parent: SATools
---

# Data Grouping and Averaging Script

The Data Grouping and Averaging Script is a Python utility designed for transforming data in CSV, ODS, or XLSX files. It groups data by date and calculates the average of values for each date.

## Features

- **Support for Multiple File Formats**: The script can load data from CSV, ODS, and XLSX files.
- **Date-Based Grouping**: Data is grouped based on the 'DATE' column.
- **Average Calculation**: Calculates the average of values for each grouped date.
- **Easy to Use**: The script can be run from the command line with input and output file paths.

## Usage

To use the script, run the following command in the terminal:

```bash
python script.py <input_file> <output_file>
```

Replace `<input_file>` with the path to your input CSV, ODS, or XLSX file and `<output_file>` with the path where you want the transformed data to be saved.

## Requirements

- Python 3
- Pandas library
- openpyxl library (for XLSX files)
- odfpy library (for ODS files)

