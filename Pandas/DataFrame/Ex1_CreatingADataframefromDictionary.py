# Write a Pandas program to create a dataframe from a dictionary and display it.
#
# Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

import pandas as pd

data= {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df = pd.DataFrame(data)
print(df.to_string())

# Write a Pandas program to create a DataFrame from a nested dictionary and flatten the multi-level columns.
# Write a Pandas program to create a DataFrame from a dictionary where values are lists of unequal lengths by filling missing values with None.
# Write a Pandas program to construct a DataFrame from a dictionary and then randomly shuffle the rows.
# Write a Pandas program to create a DataFrame from a dictionary and then transpose it, ensuring that data types remain consistent.