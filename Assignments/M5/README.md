# Milestone Assignment 2: Principal Component Analysis

## Files

- `Assignment5.py`: Spark data preparation and two-component PCA.
- `breast_cancer_referrals.csv`: supplied referral records.
- `README.md`: run instructions.

## Run

Use Python 3.10 or later, Apache Spark 4.x (PySpark), NumPy, and Java 21.
Set JAVA_HOME to your Java installation and ensure Python and Java are on PATH.
Install PySpark in your Python environment if needed:

```powershell
python -m pip install pyspark numpy
python Assignment5.py
```

The script uses paths relative to itself. No installed libraries are bundled.
It runs Spark locally, prints the results, and creates `results.txt`.

## Steps

1. Load the supplied CSV with an explicit schema: patient ID and diagnosis
   are strings; the 30 measurements are doubles.
2. Remove exact duplicate rows and count missing measurement values.
3. Fill missing measurements with medians using Spark's Imputer.
4. Assemble the measurements and standardize them to zero mean and unit
   sample standard deviation.
5. Fit PCA with two components and report each explained-variance proportion
   and their total.
6. Print the five largest absolute feature weights for each component.

Patient ID and diagnosis are excluded from the feature vector. Missing IDs
or diagnoses do not affect PCA because they are not predictors. The optional
logistic regression is omitted. PCA is fitted to the full cleaned dataset
for descriptive analysis; feature weights are not clinical or funding recommendations.

## Results

The 572 input rows become 569 after removing three duplicates. Each of
mean_radius, mean_texture, and worst_area has six missing values.
PC1 explains 44.2335% of the variance and PC2 explains 18.9672%,
giving 63.2007% combined. Tested with PySpark 4.2.0 and Java 21.
