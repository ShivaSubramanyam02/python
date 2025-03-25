class Circle:
    
    
    @staticmethod
    def pi_value():
        return 3.1416
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.pi_value() * self.radius ** 2
    
    def circumference(self):
        return 2 * Circle.pi_value() * self.radius
    
    

circle1 = Circle(10)
circle2 = Circle(5)



print(f"Circle with radius {circle1.radius}: Area = {circle1.area()}, Circumference = {circle1.circumference()}")
print(f"Circle with radius {circle2.radius}: Area = {circle2.area()}, Circumference = {circle2.circumference()}")
