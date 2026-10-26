# Module 4 Assignment: Netflix Data Visualization

## Submission files

- `Assignment4.py`: prepares and cleans the dataset, describes the data,
  calculates descriptive statistics, and creates genre and rating charts.
- `Assignment4.R`: recreates the genre chart from the Python genre-count CSV.
- `netflix_data.zip`: input dataset containing `netflix_data.csv`.
- `README.md`: instructions for running and understanding the solution.

## How to run

Use Python 3 with pandas, matplotlib, and seaborn installed, and R.
No installed packages are bundled. R uses built-in functions only.

1. Extract the submission archive and open its Solution folder in a terminal.
2. Run `python Assignment4.py`.
3. From the same folder, run `Rscript Assignment4.R`. In RStudio, set the
   working directory to the script's folder before running it.

Python extracts the data as `Netflix_shows_movies.csv`, saves
`Netflix_shows_movies_cleaned.csv`, and generates `analysis.txt`,
`top_genres.csv`, `genres_python.png`, and `ratings_python.png`.
R reads `top_genres.csv` and generates `genres_r.png`.
These results are generated when the code runs, rather than bundled.
Repeated runs overwrite these generated files.

## Understanding the analysis

Missing text values, including missing date strings, are labeled Unknown;
exact duplicate rows are removed. Dates are not invented or used in date
calculations. Descriptive statistics include release-year count, mean,
standard deviation, quartiles, and range, plus categorical summaries.

The dataset contains no watch counts, so the requested most watched genres
cannot be established. The genre charts show catalog frequency instead.
Comma-separated genres are counted individually; a title can belong to
several categories. Ratings describe maturity classifications rather than
viewer scores. The results describe the supplied catalog snapshot.
