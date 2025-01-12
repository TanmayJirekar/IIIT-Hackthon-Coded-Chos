import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape data (replace with a Bollywood-specific website)
url = "https://www.imdb.com/chart/top/"  # Replace this with an actual Bollywood movie source

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract movie titles and ratings (example scraping for IMDb)
movies = soup.select("td.titleColumn a")
ratings = soup.select("td.ratingColumn strong")

# Extract data into lists
movie_titles = [movie.text for movie in movies[:10]]
movie_ratings = [float(rating.text) for rating in ratings[:10]]

# Create a DataFrame
scraped_data = pd.DataFrame({
    "movie_title": movie_titles,
    "imdb_rating": movie_ratings,
})

print("Scraped Data:\n", scraped_data)

# Save scraped data to CSV
scraped_data.to_csv("scraped_movies.csv", index=False)
print("\nScraped data saved to 'scraped_movies.csv'")
