import pandas as pd

# Load data from the CSV file
bollywood_df = pd.read_csv("bollywood_data.csv")

# Group by genre and calculate total box office collections
genre_box_office = bollywood_df.groupby("genre")["box_office_crores"].sum()

# Group by release year and calculate total box office collections
yearly_box_office = bollywood_df.groupby("release_year")["box_office_crores"].sum()

# Print results
print("Box Office Collection by Genre:\n", genre_box_office)
print("\nBox Office Collection by Year:\n", yearly_box_office)

# Save results to CSV files
genre_box_office.to_csv("genre_box_office.csv")
yearly_box_office.to_csv("yearly_box_office.csv")
print("\nAnalysis saved to 'genre_box_office.csv' and 'yearly_box_office.csv'")
