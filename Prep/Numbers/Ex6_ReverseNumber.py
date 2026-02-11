 # 6.) Python program to Reverse Number

num = int(input("Enter a number"))

rev = 0

while num >0:
    rev = (num%10)+rev*10
    num =int(num/10)

print(f"Reversed number is {rev}")