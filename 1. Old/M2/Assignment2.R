library(utils)

# Unzip a zipped file
zipped_file <- 'Employee Profile.zip'
unzip(zipped_file)

# Read a csv file inside a zipped file 
# Read on the fly without requiring unzipping
df <- read.csv(unz(zipped_file, 'Employee Profile.csv'))

print(df)
