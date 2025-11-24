# Write a Python program to create an array of 5 integers and display the array items. Access individual elements
# through indexes.
# Sample Output:
# 1
# 3
# 5
# 7
# 9
# Access first three items individually
# 1
# 3
# 5

arr = [1, 3, 5, 7, 9]
l = len(arr)
for i in range(0,l):
    print(arr[i])

print("Access first three items individually")
print(arr[0])
print(arr[1])
print(arr[2])