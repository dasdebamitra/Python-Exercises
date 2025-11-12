# Write a Pandas program to change the data type of given a column or a Series.
#
# Sample Series:
#     Original Data Series:
# 0       100
# 1       200
# 2    python
# 3    300.12
# 4       400
# dtype: object
# Change the said data type to numeric:
# 0    100.00
# 1    200.00
# 2       NaN
# 3    300.12
# 4    400.00
# dtype: float64

import pandas as pd

list_data = pd.Series([100,200,"python",300.12,400])
print("Original Data Series:\n",list_data)

numeric_series = pd.to_numeric(list_data,errors='coerce')
print("Change the said data type to numeric:\n",numeric_series)

# Write a Pandas program to change the data type of a Series from string to numeric and handle conversion errors gracefully.
# Write a Pandas program to convert a Series of mixed types to datetime and filter out invalid dates.
# Write a Pandas program to convert a Series containing numeric strings with commas to floats.
# Write a Pandas program to change the data type of a Series to categorical and then display the category codes.

