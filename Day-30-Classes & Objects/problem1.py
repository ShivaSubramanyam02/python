class car:
    def __init__(self,model,brand,year):
        self.model = model
        self.brand = brand
        self.year = year
        
    def displau_info(self):
         print(f"Car Details: {self.year} {self.brand} {self.model}")
         
my_car = car("toyata","hilux",2025)

my_car.displau_info()
        
        

    