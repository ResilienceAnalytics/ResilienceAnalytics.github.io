---
layout: default
title: About
nav_exclude: false
nav_order: 1
child_nav_order: reversed
parent : Modeling
grand_parent : SATools
---

# Regression Analysis Tool Documentation

## Overview
This documentation provides guidance on how to use the `Regression.py` script for performing linear regression analysis. The script requires an ODS file containing the dataset for analysis and command-line arguments specifying the variables and parameters for the regression.

## Requirements
- Python environment (preferably 3.7+)
- Libraries: pandas, numpy, scikit-learn
- An ODS file with structured data, including a 'DATE' column

## Usage
To run the script, you should use the following command format in your terminal:

```shell
python Regression.py <path_to_ods_file> '<independent_vars | dependent_var>' <nan_strategy> <start_date> <end_date>
```

### Arguments
- `<path_to_ods_file>`: The file path to the ODS file containing your dataset.
- `<independent_vars | dependent_var>`: A string of independent variable names separated by spaces, followed by a pipe character (`|`), and then the dependent variable name.
- `<nan_strategy>`: Strategy for handling missing values. Options are 'mean', 'median' or 'drop'.
- `<start_date>`: The starting date for the data analysis in `YYYY-MM-DD` format.
- `<end_date>`: The ending date for the data analysis in `YYYY-MM-DD` format.

### Example
```shell
python Regression.py final_data_for_regression_imputed.ods 'M2SL | Debt' median 2020-01-01 2021-01-01
```

## Output
The script will output the following information after successful execution:
- Coefficients: The coefficients of the independent variables in the regression equation.
- Interception: The intercept of the regression line.
- Coefficient of determination (R²): Indicates how well the independent variables explain the variance of the dependent variable.
- Mean Squared Error (MSE): The mean of the squares of the errors between the actual and predicted values.

### Example Output
```
Coefficients: [1.67854063]
Interception: -4073.9310277542318
Coefficient of determination (R²): 0.8142514713061934
Mean Squared Error (MSE): 745936.8563022901
```

## Interpretation of Output
- **Coefficients**: A coefficient value tells you the change in the dependent variable for a one-unit change in the independent variable while holding other variables constant.
- **Interception**: This is the value of the dependent variable when all independent variables are zero.
- **Coefficient of determination (R²)**: A value close to 1 indicates a strong relationship, whereas a value close to 0 indicates a weak relationship between independent and dependent variables.
- **Mean Squared Error (MSE)**: A lower MSE indicates a better fit for the model to the data.

For further assistance or more information, please refer to the official documentation of the libraries used or contact the support.
