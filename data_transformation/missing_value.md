---
layout: default
title: Missing Value
nav_exclude: false
nav_order: 5
child_nav_order: reversed
parent: Data Transformation
grand_parent: SATools
---

# Missing Value

This document provides a guide to the Python script used for handling missing values in datasets. The script can load data from CSV, XLSX, or ODS files. If the input file is in CSV or XLSX format, it is automatically converted to an ODS file for processing. The main functionality of the script is to fill missing values (NaNs) in a specified column of the dataset.

## Functionality

- **Load and Convert Data**: If the input file is in CSV or XLSX format, it is converted to the ODS format.
- **Fill Missing Values**: The script fills missing values in the specified column. It first fills NaN values at the start of the series using backward filling. Then, it handles intermediate NaN values by replacing them with the last valid (non-NaN) value encountered.

## Usage

To use the script, run it from the command line with the file path and column name as arguments:

```bash
python script.py <file_path> <column_name>

The script outputs the converted input file (if applicable) and the processed file, both in ODS format.
