class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
obj = Circle(5)
print("Perimeter of the circle:", obj.perimeter())
print("Area of the circle:", obj.area())