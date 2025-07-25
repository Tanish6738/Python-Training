# Person Class with Age Calculation

# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    def calculate_age(self, current_year):
        return current_year - self.date_of_birth
    
obj = Person("Alice", "USA", 2004)
print("Name:", obj.name)
print("Country:", obj.country)
print("Age:", obj.calculate_age(2025))