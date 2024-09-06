# Highridge Construction Company Payment Slips

This repository has two files, Python and R scripts. They are both doing the same task of generating (and printing) the payment slips of 400 workers of Highridge Construction Company.

## Python Script: Assignment1.py
- Generates a list of 400 workers with random salaries between 1,000 and 50,000 and sex "Female/ Male" using `random` module.
- Using if statements, it assigns employees levels based on their salaries and sexes.
- Exception handling is included.
- It does not require any external libraries for it to work. It uses Python's in-built features.

## R Script: Assignment1.R
- This is a translatation of Python script into R version.
- It uses in-built function `sample` for randomizing salaries between 1,000 and 50,000 and choosing sex "Female/ Male"
- Performs the same functions: worker generation, employee level assignment, and exception handling.
- It also does not require any external libraries

## Instructions:
1. Open and run the `Assignment1.py` Python script in any Python environment such as Python's IDLE.
2. Open and run the `Assignment1.R` R script in any R environment such as the default R environment.

## Note
- I opted to put the second given condition on top since it is more specific than the first and will be, for the most part, missed if we put the first conition on top since also their ranges largely intersects.

