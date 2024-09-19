# Load necessary libraries
library(ggplot2)

# Load the dataset from the CSV file
genres_data <- read.csv('most_watched_genres.csv', stringsAsFactors = FALSE)

# Rename the columns for clarity
colnames(genres_data) <- c("Genre", "Count")

# Plot Most Watched Genres using ggplot2
ggplot(genres_data, aes(x=Count, y=reorder(Genre, Count))) +
  geom_bar(stat='identity', fill='steelblue') +
  theme_minimal() +
  ggtitle('Top 10 Most Watched Genres on Netflix') +
  xlab('Count') +
  ylab('Genre') +
  theme(axis.text.y = element_text(size=10))
