# Milestone Assignment 2: Principal Component Analysis

## Overview
This assignment is about developing a model to address a growing number of referrals at Anderson Cancer Center.

## Files
- `Assignment5.py`: Main program.
- `README.md`: This file explaining what the program does step by step.
- `breast_cancer_referrals.csv`: Dataset used in the analysis.

## Requirements
- Latest versions of Python 3
- Required packages: Apache Spark 4.x (PySpark), NumPy
- Java 21

## How to Run
- Install the required packages: 
- Set JAVA_HOME to your Java installation
- Make sure that Python and Java are on PATH

```powershell
python -m pip install pyspark numpy
python Assignment5.py
```

## Approach
The script goes through the following steps
- Loads data from a csv file `breast_cancer_referrals.csv`
- Cleanse data by removing duplicate records and filling missing values with median values, selected as it is normally not affected by extreme values.
- Data is then standardizes making sure that larger units do not dominate smaller units
- Principal Component Analysis PCA is then applied to reduce 30 features into two components
- Apply logistic regression on preprocessed data as a bonus step

## Results
- 3 duplicate records are removed remaining with 569 unique records
- 30 features are reduced by PCA into 2 components that explains about 63.20% of total variance
- Concavity measurements and fractal-dimension measurements had strong contributions to PC1 and PC2 respectively
- Logistics regresion achieved a prediction accuracy of 93.02% on 86 test records (85/15 train-test split)
- Text file `results.txt` containing results summaries of data cleansing to regression will be automatically generated after fully execution of `Assignment5.py` program.
