# Data Importation

# Pre-requisites
# import pandas library
import pandas as pd
import pprint

# difine the file path/location

path = "https://afterwork.ai/ds/ch/sales_trv5e.csv"

# read the csv data

sales_data = pd.read_csv(path)

# view the data 

pprint.pprint(sales_data.head())

# Data Exploration
print("====="*30)
print(f"info {sales_data.info()}")
print("====="*30)
print(f"shape {sales_data.shape}")
print("====="*30)
print(f"description : {sales_data.describe()}")


# Filtering data based on a condition (e.g., where 'Payment Method' is 'cash') using boolean indexing
print("====="*30)
active_users = sales_data[sales_data["Payment Method"] == "Cash"]

print(active_users.head())
print("====="*30)

# Selecting specific columns 'Salesperson','Region','Product','Quantity','Sales Amount' using .loc[]

selected_columns = sales_data.loc[:,["Salesperson","Region","Product","Quantity","Sales Amount"]]

print(selected_columns.head())

print("====="*30)
# Check for missing values in the dataset

sales_data_missing_values = sales_data.isnull().sum()
print(sales_data_missing_values)

print("====="*30)
