# 2. Sum All Numbers in a List
#
# Write a Python function to sum all the numbers in a list.
#
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sumOfNosInList(sum):
    add = 0
    for i in range(len(sum)):
        add += sum[i]
    return add

sum = (8, 2, 3, 0, 7)
print("Sum of List :",sumOfNosInList(sum))