import pandas as pd  # pandas for CSV handling

# Load dataset
df = pd.read_csv('spotify_music_data.csv')  # doing this to load data from CSV

# Check if 'streams' column exists before analyzing
if 'streams' in df.columns:
    # Sort songs by streams and select top 10
    most_streamed = df[['track_name', 'artist', 'streams']].sort_values(by='streams', ascending=False).head(10)  # doing this to get most streamed songs

    print("Top 10 Most Streamed Songs:")  # print heading
    print(most_streamed.to_string(index=False))  # print songs with artist and streams count without row numbers
else:
    print("Streams column not found in dataset.")  # warn if column missing
