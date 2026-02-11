# 1. Maximum of Three Numbers
#
# Write a Python function to find the maximum of three numbers.

def maxOf3Numbers(x,y,z):
    if x >= y and x >= z:
        return x
    if y >= x and y >= x:
        return y
    if z >= x and z >= y:
        return z

    return None

x = int(input("Enter number"))
y = int(input("Enter number"))
z = int(input("Enter number"))

highest = maxOf3Numbers(x,y,z)
print("Highest Number is ",highest)