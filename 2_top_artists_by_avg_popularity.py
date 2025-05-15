import pandas as pd  # Import pandas for data handling
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Load dataset
df = pd.read_csv('spotify_music_data.csv')  # doing this to load data

# Group by artist and calculate average popularity, then sort descending and take top 10
artist_popularity = df.groupby('artist')['popularity'].mean().sort_values(ascending=False).head(10)  # doing this to find most popular artists on average

# Print top 10 artists by average popularity
print('Top 10 Artists by Average Popularity:')
print(artist_popularity)  # doing this to show the numeric results in console

# Plot horizontal bar chart of top artists by average popularity
plt.figure(figsize=(10,6))  # doing this to set figure size
artist_popularity.plot(kind='barh', color='skyblue')  # doing this to plot horizontal bars
plt.title('Top 10 Artists by Average Popularity')  # doing this to set the title
plt.xlabel('Average Popularity Score')  # doing this to label x-axis
plt.ylabel('Artist')  # doing this to label y-axis
plt.gca().invert_yaxis()  # doing this to invert y-axis so top artist is on top
plt.tight_layout()  # doing this to adjust layout nicely
plt.show()  # doing this to display the plot
