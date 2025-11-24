#Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius

print("Type 1 if you want to enter temperature in Celcius")
print("Type 2 if you want to enter temperature in Farenheit")

response =input()

if(int(response) != 1) and (int(response) != 2):
    print("Invalid Input. Temperature cannot be calculated")

if int(response) ==1:
    c = int(input("Enter temperature in Celcius"))
    F = ((c/5)*9) + 32
    print("Temperature in Farenheit is ",F)

if int(response) == 2:
     f = int(input("Enter temperature in Farenheit"))
     C = ((f-32)/9)*5
     print("Temperature in Celcius is ",C)



