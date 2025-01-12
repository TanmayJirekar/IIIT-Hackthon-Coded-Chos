import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bollywood_df = pd.read_csv("bollywood_data.csv")

genre_box_office = bollywood_df.groupby("genre")["box_office_crores"].sum()
yearly_box_office = bollywood_df.groupby("release_year")["box_office_crores"].sum()


plt.figure(figsize=(8, 5))
sns.barplot(x=genre_box_office.index, y=genre_box_office.values)
plt.title("Total Box Office Collection by Genre")
plt.xlabel("Genre")
plt.ylabel("Box Office Collection (Crores)")
plt.savefig("box_office_by_genre.png")  # Save plot
plt.show()

# Plot yearly box office collection trends
plt.figure(figsize=(8, 5))
sns.lineplot(x=yearly_box_office.index, y=yearly_box_office.values, marker="o")
plt.title("Box Office Collection Trends Over Years")
plt.xlabel("Release Year")
plt.ylabel("Box Office Collection (Crores)")
plt.savefig("box_office_trends_by_year.png")  # Save plot
plt.show()
