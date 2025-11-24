# Write a Python program to create a person class.
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age

from datetime import date

class Person:
    def __init__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calcAge(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month:
            age = age -1
        return age

    def displayDetails(self):
        age = self.calcAge()
        print("Name:",self.name,"Age:",age,"Country:",self.country)

person1 = Person("Harry","UK",date(1982,11,10))
person1.displayDetails()
person2 = Person("John","Ireland",date(1978,5,24))
person2.displayDetails()
person3 = Person("William","USA",date(2002,9,18))
person3.displayDetails()