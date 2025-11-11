# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

import pandas as pd

series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

ds = series1+series2
print("Addition of series:\n",ds)
ds = series1-series2
print("Difference of series:\n", ds)
ds = series1*series2
print("Multiplication of series:\n", ds)
ds = series1/series2
print("Division of series:\n", ds)

# Write a Pandas program to compare two Series and return a Series of booleans indicating if elements are within a tolerance of 5%.
# Write a Pandas program to compare two Series element-wise and identify indices where the absolute difference exceeds a threshold.
# Write a Pandas program to compare two Series and return a Series with 'Equal' or 'Not Equal' based on element matching.
# Write a Pandas program to compare two Series of strings and return the indices where strings differ in length.



