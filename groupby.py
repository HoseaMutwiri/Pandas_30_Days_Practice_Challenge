# import pandas library

import pandas as pd

# Load the dataset from the provided URL

sales_data_2 = pd.read_csv('https://archive.org/download/sales_smzxa/sales_smzxa.csv')

# Grouping the data by 'Location' and calculating the total memory for each location

grouped_data = sales_data_2.groupby("Location")["Operating System"].count().reset_index()

print(grouped_data)

# Create a boolean mask to filter servers with a cpu core greater than 8

mask = sales_data_2["CPU Cores"]>8

# Apply the boolean mask to filter the dataset

masked_data = sales_data_2[mask]

# Display the filtered dataset

print(masked_data.head())