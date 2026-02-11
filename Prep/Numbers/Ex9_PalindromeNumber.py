# 9.) Python program to find Palindrome number

num = int(input("Enter a number"))

nums = num
rev = 0

while nums>0:
    rev = rev*10 + (nums%10)
    nums = int(nums/10)

if num == rev:
    print(f"{num} is Palindrome Number")
else:
    print(f"{num} is not Palindrome Number")