# Write a Python program to get the number of occurrences of a specified element in an array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 3, 7, 9, 3])
# Number of occurrences of the number 3 in the said array: 3

from array import *

array_num = array('i', [1, 3, 5, 3, 7, 9, 3])

l = len(array_num)

for i in range(0,l-1):
    num = array_num[i]
    count = 1
    for j in range(1,l):
        if array_num[i] == array_num[j]:
            count = count+1
    print("Item:",num," Count:",count)

