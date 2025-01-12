import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load data from the CSV file
bollywood_df = pd.read_csv("bollywood_data.csv")

# Generate word cloud for genres
wordcloud_genre = WordCloud(width=800, height=400, background_color="white").generate(" ".join(bollywood_df["genre"]))

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_genre, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Movie Genres")
plt.savefig("wordcloud_genre.png")  # Save the word cloud as an image
plt.show()
