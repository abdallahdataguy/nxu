# Module 4 Assignment: R Integration
# Run from the Solution folder after running Assignment4.py.

genres <- read.csv('top_genres.csv', stringsAsFactors = FALSE)
png('genres_r.png', width = 1600, height = 1000, res = 150)
par(mar = c(5, 12, 4, 2))
barplot(rev(genres$Count), names.arg = rev(genres$Genre),
        horiz = TRUE, las = 1, col = 'steelblue', border = NA,
        main = 'Top 10 Netflix Genres by Catalog Count',
        xlab = 'Number of titles (not viewing counts)')
invisible(dev.off())
