# 4. Reverse a String
#
# Write a Python program to reverse a string.
#
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse(str):
    rev = ""
    for i in str:
        rev = i + rev
    return rev

str = "1234abcd"
print("Reversed String :",reverse(str))


