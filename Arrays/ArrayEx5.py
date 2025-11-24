# Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents. Also, find the size of the memory buffer in bytes.
# Sample Output:
# Original array: array('i', [1, 3, 5, 7, 9])
# Current memory address and the length in elements of the buffer: (139741883429512, 5)
# The size of the memory buffer in bytes: 20

from array import *

original_array = array('i', [1, 3, 5, 7, 9])

print("Current memory address and the length in elements of the buffer",str(original_array.buffer_info()),len(original_array))
print("Size of memory buffer:",original_array.buffer_info()*original_array.itemsize)
