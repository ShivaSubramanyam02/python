class employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
        
    def annual_salary(self):
        return self.salary * 12
    
    
    
emp1 = employee("subbu",100000,"python developer")
emp2 = employee("tony",500,"internship")

print(emp2.annual_salary())