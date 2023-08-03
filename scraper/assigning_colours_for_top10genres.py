import pandas as pd
import random

# Predefined list of color names
color_names = ["red", "green", "blue", "pink", "purple", "orange", "yellow", "brown", "cyan", "magenta",
               "teal", "lime", "indigo", "lavender", "maroon", "olive", "coral", "navy", "gold", "silver",
               "crimson", "turquoise", "orchid", "slateblue", "peru", "tomato", "chocolate", "seagreen", "rosybrown",
               "darkorange", "mediumvioletred", "darkslategray", "darkkhaki", "mediumblue", "mediumseagreen", "cadetblue", "firebrick", "palevioletred", "darkcyan",
               "limegreen", "saddlebrown", "darkviolet", "darkgoldenrod", "steelblue", "sienna", "forestgreen", "darkturquoise", "salmon", "deepskyblue",
               "mediumorchid", "dodgerblue", "orangered", "purple", "mediumslateblue", "indianred", "royalblue", "mediumspringgreen", "deeppink", "slategrey"]

# Read the CSV file into a DataFrame
df = pd.read_csv("book_details_10common_genres.csv")

# Create a dictionary to store genre-color mappings
genre_color_map = {}

# Function to assign colors to genres
def assign_color(genres):
    assigned_colors = []
    for genre in eval(genres):
        if genre not in genre_color_map:
            genre_color_map[genre] = random.choice(color_names)
        assigned_colors.append(genre_color_map[genre])
    return assigned_colors

# Assign colors to genres in the top_genres column
df['cover_page_colours'] = df['top_genres'].apply(assign_color)

# Save the updated DataFrame to a new CSV file
df.to_csv("book_details_with_50colors.csv", index=False)
