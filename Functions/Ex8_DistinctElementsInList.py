# 8. Return a New List with Distinct Elements from a List
#
# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def removeDuplicates(list):
    unique = ()
    for i in list:
        if i not in unique:
            unique = unique + (i,)
    return unique

sample_list = [1,2,3,3,3,3,4,5]
unique_list = removeDuplicates(sample_list)
print(unique_list)