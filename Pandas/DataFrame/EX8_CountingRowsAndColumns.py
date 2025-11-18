# Write a Pandas program to count the number of rows and columns of a DataFrame.
#
# Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# Expected Output:
# Number of Rows: 10
# Number of Columns: 4

import pandas as pd
import numpy as np
from numpy.ma.core import count

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
print("No. of rows:", str(len(df.axes[0])))
print("No. of columns:",str(len(df.axes[1])))

# Write a Pandas program to count the number of rows and columns of a DataFrame and then print a formatted string showing both counts.
# Write a Pandas program to count rows and columns, then verify that the product equals the total number of elements in the DataFrame.
# Write a Pandas program to count the number of rows and columns and then check if any column has zero non-NaN values.
# Write a Pandas program to count rows and columns and then add these counts as new columns to an existing DataFrame.