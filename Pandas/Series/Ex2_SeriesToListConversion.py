# Write a Pandas program to convert a Panda module Series to Python list and it's type.

import pandas as pd

ds = pd.Series([2,4,6,8,10])
print(ds)
print(type(ds))
print("Convert Pandas Series to List")
print(ds.tolist())
print(type(ds.tolist()))

# Write a Pandas program to convert a Series containing mixed numeric types to a Python list and
# then filter out non-integer values.
# Write a Pandas program to convert a Series of boolean values to a Python list and verify its type.
# Write a Pandas program to convert a Series of string numbers to a Python list, then cast them to integers.
# Write a Pandas program to convert a Series with missing values to a Python list and count the number of
# None entries.
