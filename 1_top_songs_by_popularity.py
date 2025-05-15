import pandas as pd  # Import pandas for data manipulation

# Load the dataset from CSV file
df = pd.read_csv('spotify_music_data.csv')  # doing this to read your Spotify data

# Sort the songs by popularity in descending order and take top 10
top_songs = df[['track_name', 'artist', 'popularity']].sort_values(by='popularity', ascending=False).head(10)  # doing this to get the top songs by popularity

# Print the top 10 songs with their artists and popularity scores
print("Top 10 Songs by Popularity:")
print(top_songs.to_string(index=False))  # doing this to display results neatly without row indices
