# Write a Python Pandas program to get the columns of the DataFrame (movies_metadata.csv file).

import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\OneDrive - Barnes & Noble College\Python Exercises\Pandas\IMDb\movies_metadata.csv')
print("Columns of the dataframe:")
print(df.columns)

# Write a Pandas program to load movies_metadata.csv and list all column names in alphabetical order.
print("Columns of the dataframe:")
print(df[sorted(df.columns)])

# Write a Pandas program to load movies_metadata.csv and display column names along with their data types.

# Write a Pandas program to extract the column names from movies_metadata.csv and save them as a Python list.
print("Column names as list:")
print(df.columns.to_list())

# Write a Pandas program to load movies_metadata.csv and print column names that contain the substring "date".