
# Spotify Music Trends Data Analysis 

This project analyzes Spotify song data to uncover trends in popularity, artist impact, genre preferences, language distribution, and streaming performance.

## Dataset

- File: `spotify_music_data.csv`
- Contents: Metadata for popular Spotify tracks including:
  - `track_name`
  - `artist`
  - `popularity`
  - `genre`
  - `language`
  - `streams`

Make sure this file is placed in the project root directory.

##  Project Structure

```
Spotify-Music-Trends-Data-Analysis/
│
├── spotify_music_data.csv
├── 1_top_songs_by_popularity.py
├── 2_top_artists_by_avg_popularity.py
├── 3_top_genres.py
├── 4_language_distribution.py
├── 5_most_streamed_songs.py
├── README.md
```

## Python Scripts

### 1. Top Songs by Popularity
- File: `1_top_songs_by_popularity.py`
- Lists the top 10 songs based on popularity score.

### 2. Top Artists by Average Popularity
- File: `2_top_artists_by_avg_popularity.py`
- Calculates the average popularity of songs for each artist and shows the top 10, with visualization.

### 3. Top Genres
- File: `3_top_genres.py`
- Displays top 10 music genres by average popularity, with a horizontal bar chart.

### 4. Language Distribution
- File: `4_language_distribution.py`
- Shows the top 10 most common languages used in songs, with a plot.

### 5. Most Streamed Songs
- File: `5_most_streamed_songs.py`
- Lists the songs with the highest number of total streams.

##  How to Run

Make sure you have the required libraries:

```bash
pip install pandas matplotlib
```

Then run each script individually:

```bash
python 1_top_songs_by_popularity.py
python 2_top_artists_by_avg_popularity.py
python 3_top_genres.py
python 4_language_distribution.py
python 5_most_streamed_songs.py
```

## Notes

- If any column is missing (like `streams` or `language`), the script will notify you.
- Make sure column names in the dataset match those used in scripts.

## 👨‍💻 Author

**Sahil Islam**  
B.Tech CSE — Data Analytics using Python Laboratory Project
