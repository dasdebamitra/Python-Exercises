# 6. Check if a Number Falls Within a Given Range
#
# Write a Python function to check whether a number falls within a given range.

def checkRange(x,y,num):
    for i in range(x,y+1):
        if num == i:
            return "In Range"
    return "Not in Range"

x= int(input("Enter lower range"))
y= int(input("Enter higher range"))
num = int(input("Enter number to match"))

print(f"{num} is {checkRange(x,y,num)} of {x} and {y}")