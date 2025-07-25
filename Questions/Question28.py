#  Calculator Class for Basic Arithmetic Operations

# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    
obj = Calculator()
print("Addition:", obj.add(10, 5))
print("Subtraction:", obj.subtract(10, 5))
print("Multiplication:", obj.multiply(10, 5))
print("Division:", obj.divide(10, 5))
