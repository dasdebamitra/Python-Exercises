# Write a Pandas program to compare the elements of the two Pandas Series.
#
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]

import pandas as pd

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])

print("Compare the series:")
print(ds1==ds2)
print("Is less than:")
print(ds1<ds2)
print("Is greater than:")
print(ds1>ds2)

# Write a Pandas program to compare two Series and return a Series of booleans indicating if elements are within a tolerance of 5%.
# Write a Pandas program to compare two Series element-wise and identify indices where the absolute difference exceeds a threshold.
# Write a Pandas program to compare two Series and return a Series with 'Equal' or 'Not Equal' based on element matching.
# Write a Pandas program to compare two Series of strings and return the indices where strings differ in length.