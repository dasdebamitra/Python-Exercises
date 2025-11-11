# Write a Pandas program to create and display a one-dimensional array-like object containing an
# array of data using Pandas module.

import pandas as pd

car_brands = ["Maruti","Hyundai","Tata","Mahindra"]
print(pd.Series(car_brands))

