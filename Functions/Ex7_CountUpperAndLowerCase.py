# 7. Count Uppercase and Lowercase Letters in a String
#
# Write a Python function that accepts a string and counts the number of upper and lower case letters.
#
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def countCase(str):
    upper = 0
    lower = 0
    for i in str:
        if i.isupper() :
            upper +=1
        if i.islower():
            lower +=1
    return upper,lower

str = 'The quick Brow Fox'
upper,lower = countCase(str)
print("No. of Upper case characters :",upper)
print("No. of Lower case Characters :",lower)
