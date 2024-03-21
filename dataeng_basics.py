# File Loading

# Reading Text Files
with open('file.txt', 'r') as f:
    data = f.read()

# Reading CSV Files using csv module:
import csv

with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Reading CSV Files using pandas library
import pandas as pd

data = pd.read_csv('file.csv')


# Reading Excel Files using pandas 
data = pd.read_excel('file.xlsx')

# Basic Data Engineering
'''
Data Cleaning:
Removing duplicates: data.drop_duplicates()
Handling missing values: data.dropna(), data.fillna(value)

Data Transformation:
Renaming columns: data.rename(columns={'old_name': 'new_name'})
Adding new columns: data['new_column'] = ...
Applying functions: data['new_column'] = data['column'].apply(func)

Data Aggregation:
Grouping data: data.groupby('column')
Aggregating data: grouped_data.agg({'column': 'sum'})

Data Filtering:
Filtering based on conditions: data[data['column'] > value]

Data Joining/Merging:
Merging dataframes: pd.merge(df1, df2, on='common_column')
Concatenating dataframes: pd.concat([df1, df2], axis=0)

Saving Data:
Saving to CSV: data.to_csv('new_file.csv', index=False)
Saving to Excel: data.to_excel('new_file.xlsx', index=False)

Libraries Used:
pandas: For data manipulation and analysis.
csv: For reading and writing CSV files.
'''
