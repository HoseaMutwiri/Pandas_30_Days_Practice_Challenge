import pandas as pd

# Load the dataset from the provided URL

sales_data_2 = pd.read_csv('https://archive.org/download/sales_smzxa/sales_smzxa.csv')

# Display the first few rows of the dataset to understand its structure
print(sales_data_2.head())

# Check for missing values in the dataset

missing_values = sales_data_2.isnull().sum()

print(missing_values)

# Fill missing values in the 'Memory (GB)' column with the mean value

sales_data_2['Memory (GB)'] = sales_data_2['Memory (GB)'].fillna(sales_data_2['Memory (GB)'].mean())

print(sales_data_2.isnull().sum())

# Drop rows with missing values in the 'Storage (TB)' column

new_data = sales_data_2.dropna(subset=['Storage (TB)'])

print(new_data.isnull().sum())


