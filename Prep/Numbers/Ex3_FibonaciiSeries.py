# 3.) Python program to find Fibonacci series upto a
# given number range

ran = int(input("Enter the range upto which Fibonacii series should be generated"))

Fibonacci = [0, 1]

for i in range(2,ran):
    Fibonacci.append(Fibonacci[i - 1] + Fibonacci[i - 2])

print(Fibonacci)

