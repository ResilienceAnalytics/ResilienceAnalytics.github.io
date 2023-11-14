---
layout: default
title: Data Grouping and Averaging Script (ODS Output)
nav_exclude: false
nav_order: 7
child_nav_order: reversed
parent: Data Transformation
grand_parent: SATools
---

# Data Grouping and Averaging Script (ODS Output)

The Data Grouping and Averaging Script is a Python utility designed for transforming data in CSV, ODS, or XLSX files. It groups data by date and calculates the average of values for each date, then saves the result to an ODS file.

## Features

- **Support for Multiple File Formats**: The script can load data from CSV, ODS, and XLSX files.
- **Date-Based Grouping**: Data is grouped based on the 'DATE' column.
- **Average Calculation**: Calculates the average of values for each grouped date.
- **ODS Output**: Transformed data is saved in an ODS file.

## Usage

To use the script, run the following command in the terminal:

```bash
python script.py <input_file> <output_file.ods>
```

Replace `<input_file>` with the path to your input CSV, ODS, or XLSX file and `<output_file.ods>` with the path where you want the transformed data to be saved in ODS format.

## Requirements

- Python 3
- Pandas library
- openpyxl library (for XLSX files)
- odfpy library (for ODS files and output)
