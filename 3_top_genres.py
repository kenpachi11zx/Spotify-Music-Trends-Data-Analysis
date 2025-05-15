import pandas as pd  # for data manipulation
import matplotlib.pyplot as plt  # for plotting graphs

# Load dataset
df = pd.read_csv('spotify_music_data.csv')  # doing this to load the CSV data

# Check if 'genre' column exists before proceeding
if 'genre' in df.columns:
    # Group by genre, calculate average popularity, sort and get top 10 genres
    genre_popularity = df.groupby('genre')['popularity'].mean().sort_values(ascending=False).head(10)  # doing this to find popular genres

    print("Top 10 Genres by Average Popularity:")  # doing this to show header
    print(genre_popularity)  # doing this to print the result in terminal

    # Plot horizontal bar chart for genre popularity
    plt.figure(figsize=(10,6))  # set figure size
    genre_popularity.plot(kind='barh', color='orange')  # plot horizontal bars
    plt.title('Top 10 Genres by Average Popularity')  # set plot title
    plt.xlabel('Average Popularity Score')  # x-axis label
    plt.ylabel('Genre')  # y-axis label
    plt.gca().invert_yaxis()  # invert y-axis for descending order
    plt.tight_layout()  # adjust layout
    plt.show()  # show plot
else:
    print("Genre column not found in dataset.")  # notify if genre column missing
