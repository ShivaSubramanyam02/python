class vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
        
    def display_info(self):
        return f"Brand: {self.brand}, Speed: {self.speed} km/h"
        
        
class Car(vehicle):
    def __init__(self, brand, speed,fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type
        
        
    def display_info(self):
        return f"Brand: {self.brand}, Speed: {self.speed} km/h, Fuel Type: {self.fuel_type}"


V1 = vehicle("Toyata",200)
C1 = Car("supra",300,"petrol")

print(V1.display_info())
print(C1.display_info())
        
    