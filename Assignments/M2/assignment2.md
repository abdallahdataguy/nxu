# Module 2 Assignment: Salary Function

## Overview
- This assignment is about using Python to read and manipulate salary data given as csv file. Data is imported using Python Jupyter notebook, retrieve details of the given employee, process the data and export it as a zipped file containing employee details. Then an accompanying R script is used to read the exported data, extract and display the employee profile.

## Files
- `main.py`: Main program.
- `requirements.txt`: Required Python packages.
- `data.csv`: Input dataset, if applicable.

## Requirements
- Python 3.x and Jupyter notebook or any IDE that can execute Python notebooks
  - Anaconda distribution is recommended as it comes with everything needed here
- latest version of R (and optionally RStudio IDE)
- Required packages: `pandas` is required for this task to run.
- Standard libraries used: `shutil`, `csv` and `pathlib`

## How to Run
- Ensure the the required packages are installed
- Open `salary_function.ipynb` using Jupyter Notebook
- Run the program cell by cell to see how each step behaves
  - You can also run entire program by selecting "Run" then "Run All Cells"
- After the entire notebook script has completed execution, then run the R script `display_employee_profile.R`

## Approach
- Start by running the notebook script first to create a zipped file of the selected employee profile
- Run the R script after the Python notebook has completed execution to unzip and display the employee details

## Results
- The R script will unzip the Employee profile, read the Excel file inside it and display the data of the selected Employee
