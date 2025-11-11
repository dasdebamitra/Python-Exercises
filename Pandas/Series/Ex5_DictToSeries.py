# Write a Pandas program to convert a dictionary to a Pandas series.
#
# Sample Series:
# Original dictionary:
# {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
#
# Converted series:
# a    100
# b    200
# c    300
# d    400
# e    800
# dtype: int64

import pandas as pd

dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print(pd.Series(dict))

# Write a Pandas program to convert a nested dictionary into a Series and flatten its hierarchical index.


# Write a Pandas program to convert a dictionary with non-string keys to a Series and then convert the keys
# to strings.
# Write a Pandas program to convert a dictionary with missing keys to a Series with a specified default
# value for missing keys.
# Write a Pandas program to convert a dictionary to a Series and then sort the Series based on the
# dictionary values in descending order.