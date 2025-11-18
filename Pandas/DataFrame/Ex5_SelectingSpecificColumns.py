# Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
#
# Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# Expected Output:
# Select specific columns:
#         name  score
# a  Anastasia   12.5
# b       Dima    9.0
# c  Katherine   16.5
# ...
# h      Laura    NaN
# i      Kevin    8.0
# j      Jonas   19.0

import numpy as np
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts':[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels,columns=['name','score'])
print(df.to_string())

# Write a Pandas program to select the 'name' and 'score' columns from a DataFrame and then sort the resulting DataFrame by 'score' in descending order.
# Write a Pandas program to extract 'name' and 'score' columns and then filter out rows where 'score' is below the average.
# Write a Pandas program to select 'name' and 'score' columns and then create a new column that concatenates the name with its score.
# Write a Pandas program to select 'name' and 'score' columns and then display only rows with duplicate names.