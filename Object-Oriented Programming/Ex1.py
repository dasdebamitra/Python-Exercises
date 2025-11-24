# Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.

import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def calcArea(self):
        area = math.pi * (self.radius ^ 2)
        return area

    def calcPerimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

circle1 = Circle(4)
print("Area of Circle:",circle1.calcArea())
print("Perimeter of circle:",circle1.calcPerimeter())
