---
layout: default
title: About
nav_exclude: false
nav_order: 21
child_nav_order: reversed
---

# Time Series Plotting Script

## Overview

This Python script is designed for plotting time series data, providing flexibility for users to select a specific date range or plot the entire dataset. Additionally, users can choose specific columns to plot. This functionality is particularly useful in exploring trends, patterns, and anomalies over time in datasets.

## Functionality

The script reads data from a CSV or Excel file, allows selection of a custom date range or the entire dataset, and plots the specified columns as time series.

### Parameters

- `file_path` (str): Path to the data file. The file should be in a CSV or Excel format.
- `start_date` (str): Start date for the plot in YYYY-MM-DD format or 'all' to include all dates.
- `end_date` (str): End date for the plot in YYYY-MM-DD format or 'all' to include all dates.
- `columns` (list of str or None): Columns to plot. If None or not specified, all columns are plotted.

### Plotting Process

- The script identifies the specified columns and date range.
- If 'all' is specified for both start_date and end_date, the script plots data for the entire date range available in the dataset.
- It generates a line plot for each specified column over the selected date range.

## Usage

To use the script, run the following command in the terminal:

```bash
python plot_time_series.py <path_to_data_file> <start_date/all> <end_date/all> [<columns>]
```

For example, to plot specific columns over the entire date range in a CSV file:

```bash
python plot_time_series.py data.csv all all column1,column2
```

Or to plot all columns over a specific date range:

```bash
python plot_time_series.py data.xlsx 2020-01-01 2020-12-31
```

## Dependencies

- pandas: For data manipulation and reading files.
- matplotlib: For creating plots.

Ensure these libraries are installed before running the script:

```bash
pip install pandas matplotlib
```

## Notes

- This script is valuable for preliminary data analysis, especially for understanding temporal dynamics in data.
- The generated plots can be used for further analysis, reports, or presentations.
- Users should ensure that the data file contains a 'DATE' column in a suitable datetime format.

