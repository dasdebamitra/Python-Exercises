# Write a Python program to create a calculator class. Include methods for basic arithmetic operations

class Calculator:

    def addition(self,num1,num2):
        return num1 + num2

    def difference(self,num1,num2):
        if num1 > num2:
            return num1 - num2
        else:
            return num2 - num1

    def multiplication(self,num1,num2):
        return num1 * num2

    def division(self,num1,num2):
        if num2 !=0:
            return num1/num2
        else:
            return "Division by 0 is not possible"


num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

calc = Calculator()

print("Sum of ",num1," and ",num2,":",calc.addition(num1,num2))
print("Difference of ",num1," and ",num2,":",calc.difference(num1,num2))
print("Multiplication of ",num1," and ",num2,":",calc.multiplication(num1,num2))
print("Division of ",num1," and ",num2,":",calc.division(num1,num2))


