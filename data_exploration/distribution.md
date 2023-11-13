---
layout: default
title: Data Distribution Visualizer
nav_exclude: false
nav_order: 4
child_nav_order: reversed
parent: Data Exploration
grand_parent: SATools
---

# Data Distribution Visualizer Script

## Overview

The Data Distribution Visualizer is a Python script designed for graphical exploration of data distributions within a dataset. It generates histograms for numerical columns and presents them in a user-friendly interface with tabbed navigation.

## Features

- Graphical User Interface (GUI) with tabbed browsing for each figure.
- Supports multiple file formats including `.csv`, `.xlsx`, and `.ods`.
- Organizes histograms in a 2x2 grid per tab for clear visualization.
- Automatically adjusts the number of tabs based on the number of numerical columns.

## How to Use

1. Ensure that Python and the required libraries (`pandas`, `matplotlib`, and `tkinter`) are installed on your system.
2. Run the script from the terminal and provide the path to your data file as an argument:

   ```bash
   python distribution.py path/to/your/datafile.csv
   ```

3. The GUI will open with the histogram tabs. Each tab contains up to 4 histograms showing the distribution of your dataset's numerical columns.

## Requirements

- Python 3.x
- Pandas: for data manipulation.
- Matplotlib: for creating histograms.
- Tkinter: for the GUI framework.
- sys and os: for reading system arguments and file operations.

Install the required Python libraries (if not already installed) using:

```bash
pip install pandas matplotlib
```

`Tkinter` is typically included with Python, but if not, it can be installed using your system's package manager.

## Usage Notes

- The script is designed for an interactive command-line experience. All operations are guided by clear prompts.
- The script can handle any number of numerical columns, dynamically creating new tabs if the number exceeds four.
- Non-numerical columns are ignored in the histogram creation process to focus on the distribution of quantitative data.

## Limitations

- The script currently does not save the figures. To keep the visual output, users must manually save the figures from the GUI.
- The script assumes that the input file is well-formatted and that numerical columns do not contain non-numeric placeholders.


