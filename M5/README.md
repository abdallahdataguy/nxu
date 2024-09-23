# Milestone Assignment 2: Principal Component Analysis

This project includes two files, a Python file `Assignment5.py`and a readme file `README.md`.

## File Descriptions:
1. `Assignment5.py`: This Python file does the following:
   - Loads the breast cancer dataset from scikit-learn module's datasets repository
   - Performs data preprocessing by standardizing data
   - Implements Principal Component Analysis PCA. Reduces data into two principal components.
   - Calculates and prints the explained variances for each principal component and overall 
   - Generates the loadings and sorts by absolute values for the two components to find the most important variables. Prints top 5 most contributing variables for each component.
   - Splits the data into training and testing data and implement a logistic regression
   - Evaluates a classification model accuracy, prints a classification accuracy, confusion matrix and classification report
   - Creates a scatter plot showing the two principal components using appropriate colors

2. `README.md`: This readme file that explains how this program works including file descriptions and how to run the program

## Overview:
- This project uses breast cancer dataset from scikit-learn module's datasets data to identify essential variables to be used in the classification model that will help in securing donor funding.

## Prerequisites:
- Make sure you have Python 3 and their required libraries installed in your machine.

## Installation Steps:
1. Clone this repository or download the ZIP file.
2. Extract the zip file (if downloaded).
3. Python: Install `pandas`, `numpy`, `matplotlib` and `sklearn` (scikit-learn) libraries

## Running the Project:
To run the project, follow these steps:
1. Navigate to the folder containing the files.
2. Run the following command in your terminal:
   - `python Assignment5.py`
   - Alternatively, you can open the `Assignment5.py` file in a Python IDE (such as the built-in IDLE), and run the module (keyboard shortcut is F5 in Microsoft Windows).
