import pandas as pd
from collections import Counter

# Read the CSV file into a DataFrame
df = pd.read_csv("book_details_3merged.csv")

# Function to get the 10 most common genres from a list of genres
def get_top_10_genres(genre_list):
    genre_counts = Counter(genre_list)
    return [genre for genre, count in genre_counts.most_common(10)]

# Get the 10 most common genres for each row and save them in a new column 'top_genres'
df['top_genres'] = df['genres'].apply(get_top_10_genres)

# Remove rows with null/empty cells
df.dropna(subset=['title', 'description'], inplace=True)

# Reset the index after removing rows
df.reset_index(drop=True, inplace=True)

# Create a new DataFrame with only the 'title', 'description', and 'top_genres' columns
new_df = df[['title', 'description', 'top_genres']]

# Save the new DataFrame to a new CSV file
new_df.to_csv("book_details_10common_genres.csv", index=False)
