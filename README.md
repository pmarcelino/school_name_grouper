# School Name Grouping Script

## Overview

This Python script is designed to process a list of school names, normalize and preprocess them for uniformity, and then group similar names together. It's particularly useful for handling variations in school names due to different formats or abbreviations.

## Features

- **Preprocessing**: Standardizes school names by replacing common abbreviations and terms.
- **Normalization**: Converts all names to lowercase for consistency.
- **Grouping**: Identifies and groups similar school names based on a similarity threshold.
- **CSV Output**: Outputs the results in a CSV file for easy review and analysis.

## Installation

No additional installation is required beyond a standard Python environment. The script uses built-in libraries: `difflib` and `csv`.

## Usage

1. **Prepare Your Data**: Create a text file named `school_names.txt` with one school name per line.
2. **Run the Script**: Execute the script `main.py` in a Python environment.
3. **Review Output**: Check the generated CSV file `grouped_schools.csv` for the grouped school names.


## Customization

- To tailor the script to your specific needs, you can modify the `replacements` dictionary in the `preprocess_name` function with any additional terms or abbreviations relevant to your dataset.
- The similarity threshold for grouping similar names is currently set to a default value (0.8). Adjust this threshold in the `group_school_names` function as per your requirement for more or less strict grouping.