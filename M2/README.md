# Module 2 Assignment: Salary Function
This repository has two files, Jupyter notebook Python file and R script.

## Jupyter notebook: Assignment2.ipynb
- Reads a csv file "Total.csv" in the current directory as a data frame df.
- Creates a function named "filter_employee_data" with one parameter "employee_name" that filters a data frame "df" based on "employee_name" value provided. Example name "GARY JIMENEZ" has been left in the code for testing.
- Exception handling is included.
- It does requires three libraries to run, `os`, `pandas`, and `zipfile` with `pandas` being the only external library out of three that requires separate installation as it is not a standard library.
- The "filter_employee_data" function returns a dictionary of filtered employee's data.
- The program then processes data by turning "EpmloyeeName" and "JobTitle" to a proper case using dictionary approach and creates a data frame of processed filtered employee's data and exports it as csv file named "Employee Profile.csv" in the same directory.
- Using `zipfile` module creates a zipped file named "Employee Profile.zip" containing "Employee Profile.csv" csv file.
- Deletes a csv file "Employee Profile.csv" using `os` module's remove function.

## R Script: Assignment2.R
- It uses the functions `unzip`, `unz` and `read.csv` from the standard library `utils` for unzipping the file "Employee Profile.zip" created in the Python script and reading and printing the contents of the "Employee Profile.csv".
- It does not require any non-standard libraries to run.

## Instructions:
- Put a jupyter notebook file, R script, and "Total.csv" file in the same folder to help Python read the file "Total.csv" and saves "Employee Profile.csv" and ".zip" in the same folder using relative file path.
- Open and run the `Assignment2.ipynb` file using Jupyter or any program that can read jupyter notebook files like Visual Studio Code and Jupyter notebook IDEs.
- Open R script in any R IDE and set the current working directory as the folder where the R script is located. this ensures that it reads the file "Employee Profile.zip" in the same folder using relative file path.
- Open and run the `Assignment2.R` R script in any R environment such as the default R environment.
