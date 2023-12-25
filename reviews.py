import pandas as pd

# Read the CSV file into a DataFrame
reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

# Calculate the average points and count of reviews per country
summary_data = reviews.groupby('country').agg({
    'country': 'size',
    'points': 'mean',
})

# Rename the 'size' column to 'count'
summary_data = summary_data.rename(columns={'country': 'count'})

# Round the 'points' column to the tenth place
summary_data['points'] = summary_data['points'].round(1)

# Change order of the columns to 'country', 'count', 'points'
summary_data = summary_data[['count', 'points']]

# Create a new DataFrame with only the selected columns
new_data = summary_data.reset_index()

# Specify the path for the new CSV file
new_file_path = "data/reviews-per-country.csv"

# Save the selected data to the new CSV file
new_data.to_csv(new_file_path, index=False)

# Print a message indicating that the new file has been created
print(f"New DataFrame created with selected columns and saved as: {new_file_path}")
