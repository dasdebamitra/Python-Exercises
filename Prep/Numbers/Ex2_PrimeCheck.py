# 2.) Python program to find Prime number

def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return "is not Prime"

    return "is Prime"

num = int(input("Enter number greater than 0"))

if num<=0:
    print("Invalid input")
else:
    print(f"{num} {checkPrime(num)}")

