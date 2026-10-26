# Module 4 Assignment: Netflix Data Visualization
## Overview
This assignment leverages skills in R and Python to read, cleanse, visualize and analyze Netflix Data and provide visual analytics.

## Files
- `Assignment4.py`: Main program built using Python.
- `Assignment4.R`: R script to accompany the main program.
- `netflix_data.zip`: Zipped file containing input csv dataset `netflix_data.csv`.

## Requirements
- Python 3.x
- R installation
- Required packages: `pandas`, `matplotlib`, `seaborn`

## How to Run
Install the required packages:

```bash
pip install pandas matplotlib seaborn
```

Run the program:

```bash
python Assignment4.py
```

## Approach
- Put all three files (`Assignment4.py`, `Assignment4.R` and `netflix_data.zip`) in the same folder
- Run the main program file first (`Assignment4.py`) and and wait until its completion followed by R script `Assignment4.R`


## Results
- Python will unzip the zipped file `netflix_data.zip` and rename the underlying csv file as `Netflix_shows_movies.csv`
- `Netflix_shows_movies.csv` will be cleaned and saved as `Netflix_shows_movies_cleaned.csv` and genarate analysis tex file named `analysis.txt`
- Filtered cleansed data summary named `top_genres.csv` will be generated and then the visualization files `genres_python.png`, and `ratings_python.png`
- R will also recreate an equivalent visualization file named `genres_r.png` from the same `top_genres.csv`
- All these files will be generated after running these two scripts and when the scripts are rerun they will override the results files.
