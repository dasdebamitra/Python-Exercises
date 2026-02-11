# 5.) Python program to Find Factorial on given Number

def factorial(num):
    if num<=0:
        return 1
    else:
        return num * factorial(num-1)

num = int(input("Enter number whose factorial is to be calculated"))
print(f"Factorial of {num} is {factorial(num)}")