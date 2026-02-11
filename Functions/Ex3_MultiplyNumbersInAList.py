# 3. Multiply All Numbers in a List
#
# Write a Python function to multiply all the numbers in a list.
#
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def Multiply(multiply):
    product = 1
    for i in range(len(multiply)):
        product *= multiply[i]
    return product

multiply = (8, 2, 3, -1, 7)
print("Product of numbers in a list :",Multiply(multiply))