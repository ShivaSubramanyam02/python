class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
rect1 = Rectangle(10,5)

print(rect1.area())
print(rect1.perimeter())
        