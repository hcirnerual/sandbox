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
