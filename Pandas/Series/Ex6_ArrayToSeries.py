# Write a Pandas program to convert a NumPy array to a Pandas series.
#
# Sample Series:
#   NumPy array:
# [10 20 30 40 50]
# Converted Pandas series:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

import pandas as pd
import numpy as np

np_array = np.array([10,20,30,40,50])
print("NumPy Array:",np_array)

print("Converted to Series",pd.Series(np_array))

# Write a Pandas program to convert a multi-dimensional NumPy array to a Series by flattening it.
# Write a Pandas program to convert a NumPy array of dates to a Series and set a datetime index.
# Write a Pandas program to convert a NumPy array to a Series and then replace negative values with their absolute values.
# Write a Pandas program to convert a NumPy array to a Series and then sort the Series based on the array values in ascending order.
