# 2_most_popular_artists.py

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('spotify_music_data.csv')

# Calculate average popularity by artist
artist_popularity = df.groupby('artist')['popularity'].mean().sort_values(ascending=False).head(10)

print('Top 10 artists by average popularity:')
print(artist_popularity)

# Bar plot
artist_popularity.plot(kind='barh', figsize=(10,6), color='skyblue')
plt.title('Top 10 Artists by Average Popularity')
plt.xlabel('Average Popularity Score')
plt.ylabel('Artist')
plt.gca().invert_yaxis()
plt.show()

# Count of tracks by artist
artist_tracks = df['artist'].value_counts().head(10)

print('\nTop 10 artists by number of tracks:')
print(artist_tracks)

# Bar plot
artist_tracks.plot(kind='barh', figsize=(10,6), color='lightgreen')
plt.title('Top 10 Artists by Number of Tracks')
plt.xlabel('Number of Tracks')
plt.ylabel('Artist')
plt.gca().invert_yaxis()
plt.show()
