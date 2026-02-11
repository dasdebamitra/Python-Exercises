# 5. Factorial of a Number
#
# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

def factorial(number):
    if number <= 0:
        return 1
    else:
        return number * factorial(number-1)


num = int(input("Enter Number"))
print("Factorial :",factorial(num))