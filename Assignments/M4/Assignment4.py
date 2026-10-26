# Module 4 Assignment: Netflix Data Visualization

# Import the required libraries and data preparation
from pathlib import Path
import zipfile
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

folder = Path(__file__).resolve().parent
with zipfile.ZipFile(folder / 'netflix_data.zip') as archive:
    (folder / 'Netflix_shows_movies.csv').write_bytes(archive.read('netflix_data.csv'))
df = pd.read_csv(folder / 'Netflix_shows_movies.csv', dtype={'show_id': 'string'})

# Data cleansing: Working on missing values and removing duplicate rows
missing_before = df.isnull().sum()
df = df.drop_duplicates().copy()
for column in df.select_dtypes(include=['object', 'string']).columns:
    df[column] = df[column].astype('string').str.strip().replace('', pd.NA).fillna('Unknown')
df = df.rename(columns={'listed_in': 'Genre'})
df.to_csv(folder / 'Netflix_shows_movies_cleaned.csv', index=False)

# Data exploration and calculating descriptive statistics
genre_counts = (df['Genre'].str.split(',').explode().str.strip()
                .value_counts().head(10).rename_axis('Genre').reset_index(name='Count'))
rating_counts = df['rating'].value_counts()
genre_counts.to_csv(folder / 'top_genres.csv', index=False)

analysis = (
    f'Shape: {df.shape}\n\n'
    f'Missing before:\n{missing_before}\n\n'
    f'Missing after:\n{df.isnull().sum()}\n\n'
    f'Statistics:\n{df.describe(include="all").to_string()}\n\n'
    f'Types:\n{df["type"].value_counts()}\n\n'
    f'Top 10 genres:\n{genre_counts.to_string(index=False)}\n\n'
    f'Ratings:\n{rating_counts}\n\n'
    'Genre counts represent catalog titles, not views.\n'
)
print(analysis)
(folder / 'analysis.txt').write_text(analysis, encoding='utf-8')

# Using Seaborn and Matplotlib's Pyplot to create Python visualizations 
sns.set_theme(style='whitegrid')
plt.figure(figsize=(11, 6))
sns.barplot(data=genre_counts, x='Count', y='Genre', color='steelblue')
plt.title('Top 10 Netflix Genres by Catalog Count')
plt.xlabel('Number of titles (not viewing counts)')
plt.tight_layout()
plt.savefig(folder / 'genres_python.png', dpi=150)
plt.close()

plt.figure(figsize=(10, 6))
sns.barplot(x=rating_counts.index, y=rating_counts.values, color='steelblue')
plt.title('Netflix Content Rating Distribution')
plt.xlabel('Maturity rating')
plt.ylabel('Number of titles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(folder / 'ratings_python.png', dpi=150)
plt.close()
