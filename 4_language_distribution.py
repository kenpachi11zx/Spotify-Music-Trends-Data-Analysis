import pandas as pd  # import pandas for data handling
import matplotlib.pyplot as plt  # import matplotlib for charts

# Load data
df = pd.read_csv('spotify_music_data.csv')  # doing this to read your CSV file

# Check for 'language' column before processing
if 'language' in df.columns:
    # Count the number of songs per language and get top 10 languages
    lang_counts = df['language'].value_counts().head(10)  # doing this to find languages with most songs

    print("Top 10 Languages by Number of Songs:")  # print heading
    print(lang_counts)  # print counts of songs per language

    # Plot horizontal bar chart for language distribution
    plt.figure(figsize=(10,6))  # figure size
    lang_counts.plot(kind='barh', color='purple')  # horizontal bar plot
    plt.title('Top 10 Languages by Number of Songs')  # title of plot
    plt.xlabel('Number of Songs')  # x-axis label
    plt.ylabel('Language')  # y-axis label
    plt.gca().invert_yaxis()  # invert y-axis to show highest first
    plt.tight_layout()  # layout adjustment
    plt.show()  # display plot
else:
    print("Language column not found in dataset.")  # warning message
