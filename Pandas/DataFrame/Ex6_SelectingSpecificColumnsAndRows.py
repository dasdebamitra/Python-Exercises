# Write a Pandas program to select the specified columns and rows from a given data frame.
#
# Sample Python dictionary data and list labels:
# Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# Expected Output:
# Select specific columns and rows:
#    score qualify
# b    9.0      no
# d    NaN      no
# f   20.0     yes
# g   14.5     yes

import numpy as np
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts':[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels,columns=['name','score'])
print(df.iloc[[1,3,5,6],[0,1]])


# Write a Pandas program to select specific columns ('name' and 'score') for rows with even-numbered indices only.
# Write a Pandas program to extract 'name' and 'score' columns for rows where the index is a vowel (assume index labels are letters).
# Write a Pandas program to select specific columns and then filter the DataFrame using a boolean mask on a different column.
# Write a Pandas program to select rows from a DataFrame by passing a list of index labels and then display only the 'name' and 'score' columns.