class student():
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def display_details(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
        
student1 = student("subbu",21,"A+")
student2 = student("barry allen",21,"B+")

student1.display_details()
student2.display_details()
