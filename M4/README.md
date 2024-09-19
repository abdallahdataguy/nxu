# Module 4 Assignment: Netflix Data Visualization

This project includes four files, a Python file `Assignment4.py`, R script `Assignment4.R`, zip file `netflix_data.zip` and a readme file `README.md`.

## File Descriptions:
1. `Assignment4.py`: This Python file does the following:
   - Reads a zipped archive `netflix_data.zip` and extracts a csv file named `netflix_data.csv`.
   - Renames the csv file and save it to the current working directory as `Netflix_shows_movies.csv`
   - Opens the saved csv file, cleanses it by renaming a column `listed_in`  to 'Genre'
   - Replaces all missing values in the resulting dataset by value "Unknown"
   - Tabulates the genres counts using the column "Genre" and extract top ten genres by counts
   - Tabulates the ratings counts using "rating" column
   - Creates a bar chart of the Top ten most viewed genres using genre counts
   - Creates a column chart using rating counts
   - Saves a genre counts as a csv file `most_watched_genres.csv` for use in R visuals
3. `Assignment4.R`: The file contains an R script that does the following:
   - Reads a csv file named 'most_watched_genres.csv'
   - Renames the columns to "Genre" and "Count"
   - Creates a bar chart of the Top ten most viewed genres using genre counts
5. `netflix_data.zip`: The file contains Netflix data used in this project
6. `README.md`: This readme file that explains how this program works including file descriptions and how to run the program

## Overview:
- This project uses Netflix data to provide visual analytics aimed at gaining insights from the Netflix data provided.

## Prerequisites:
- Make sure you have Python 3 and R and their required libraries installed in your machine.

## Installation Steps:
1. Clone this repository or download the ZIP file.
2. Extract the zip file (if downloaded).
3. Ensure that the following files are in the same directory:
   - `Assignment4.py`
   - `Assignment4.R`
   - `netflix_data.zip`
4. Python: Install `pandas`, `matplotlib` and `seaborn` libraries. `os` and `zipfile` are standard libraries and they come with base installation of Python.
5. R: Install `ggplot2` library. The best practice is to install all tidyverse packages by running `install.packages("tidyverse")` command.

## Running the Project:
To run the project, follow these steps:
1. Navigate to the folder containing the files.
2. Run the following command in your terminal:
   - `python Assignment4.py`
   - Alternatively, you can open the `Assignment4.py` file in a Python IDE (such as the built-in IDLE), and run the module (keyboard shorcut is F5 in Microsoft Windows).
3. After Python script is executed, open R script named `Assignment4.R` in any R environment, Rstudio preferred.
4. In RStudio, right click the tab of the opened R file and select "Set Working Directory".
   - This option sets the directory where the opened R script is contained as the current working directory.
   - This option helps R read the rest of the files relative to the R script removing the neccessity of specifying full file paths. 
