# Write a Pandas program to convert the first column of a DataFrame as a Series.
#
# Original DataFrame
#    col1  col2  col3
# 0     1     4     7
# 1     2     5     5
# 2     3     6     8
# 3     4     9    12
# 4     7     5     1
# 5    11     0    11
#
# 1st column as a Series:
# 0     1
# 1     2
# 2     3
# 3     4
# 4     7
# 5    11
# Name: col1, dtype: int64
# <class 'pandas.core.series.Series'>

import pandas as pd

d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
print("Original DataFrame:")
print(pd.DataFrame(d))
print("1st column as a Series:")
print(pd.DataFrame(d).iloc[:,0])

# Write a Pandas program to extract a specific column from a DataFrame as a Series and then rename its index using a custom function.
# Write a Pandas program to convert multiple columns of a DataFrame to separate Series and then merge them based on index.
# Write a Pandas program to convert a DataFrame's first column to a Series and fill missing values with the column mean.
# Write a Pandas program to extract a DataFrame column as a Series and then reverse the order of the Series.



