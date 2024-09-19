# Module 4 Assignment: Netflix Data Visualization

# Step 0: Import the neccessary packages
import pandas as pd
import zipfile
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Data Preparation
# Unzip the dataset
folder = r'C:\Users\ABDALLAH\Documents\GitHub\nxu\M4'
os.chdir(folder) # Set the folder as cwd

# Remove netfilx_data.csv if it exists
if os.path.exists('netflix_data.csv'):
    os.remove('netflix_data.csv')

# Extract the file
try:
    with zipfile.ZipFile('netflix_data.zip', 'r') as zip_ref:
        # Extract the specific file named 'netflix_data.csv'
        extracted = zip_ref.extract('netflix_data.csv', os.getcwd())
       
        # Rename the extracted file to 'myfile.csv'
        os.rename(extracted, os.path.join(os.getcwd(), 'Netflix_shows_movies.csv'))
except Exception as e:
    print(f'File processing error: {e}') 

# Load the dataset
df = pd.read_csv('Netflix_shows_movies.csv')

# Step 2: Data Cleaning
# Fill missing values
# Update the dataset by setting the missing data values to Unknown
df = df.fillna('Unknown')

# Rename the column 'listed_in' to 'Genres'
df = df.rename(columns={'listed_in': 'Genre'})

# Confirm there are no missing values left
print("Missing values after cleaning:\n", df.isnull().sum())

# Step 3: Data Exploration
# Descriptive statistics
print("Descriptive statistics:\n", df.describe(include='all'))

# Most watched genres (top 10)
genre_counts = df['Genre'].value_counts().head(10).reset_index()
print("\nTop 10 Most Watched Genres:\n", genre_counts)

# Save the 'Most Watched Genres' data to a CSV file for use in R
genre_counts.to_csv('most_watched_genres.csv', index=False)

# Ratings distribution
rating_counts = df['rating'].value_counts()
print("\nRatings Distribution:\n", rating_counts)

# Step 4: Data Visualization
# Set the plot style
sns.set(style="whitegrid")

# Plot Most Watched Genres
plt.figure(figsize=(10, 6))
sns.barplot(
    data=genre_counts, 
    x='count', 
    y='Genre', 
    palette='Blues_d',
    hue='Genre',  
    dodge=False,  # Ensures hues are not split into bars
    legend=False  # Disable legend
)
plt.title('Top 10 Most Watched Genres on Netflix')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()

# Plot Ratings Distribution
plt.figure(figsize=(10, 6))
sns.barplot(
    x=rating_counts.index, 
    y=rating_counts.values, 
    palette="coolwarm", 
    hue=rating_counts.index,  # Assign x variable to hue
    dodge=False,  # Disable dodge to prevent splitting bars
    legend=False  # Disable the legend
)
plt.title('Ratings Distribution on Netflix')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
