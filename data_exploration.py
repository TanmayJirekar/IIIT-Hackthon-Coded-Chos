# Import required libraries
import pandas as pd

# Sample Bollywood Movie Data (Replace with actual data later)
data = {
    "movie_title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E", "Movie F", 
                    "Movie G", "Movie H", "Movie I", "Movie J"],
    "genre": ["Action", "Romance", "Comedy", "Drama", "Action", "Comedy", 
              "Romance", "Thriller", "Drama", "Action"],
    "release_year": [2023, 2022, 2023, 2021, 2022, 2020, 2020, 2022, 2021, 2023],
    "box_office_crores": [150, 80, 120, 60, 200, 100, 90, 70, 50, 180],
    "lead_actor": ["Actor X", "Actor Y", "Actor Z", "Actor X", "Actor Y", "Actor Z", 
                   "Actor X", "Actor Z", "Actor Y", "Actor X"],
}

# Convert data to DataFrame
bollywood_df = pd.DataFrame(data)

# Display basic data exploration results
print("First 5 Rows of Data:\n", bollywood_df.head())
print("\nData Information:")
print(bollywood_df.info())

# Save data to CSV for later use
bollywood_df.to_csv("bollywood_data.csv", index=False)
print("\nData saved to 'bollywood_data.csv'")
