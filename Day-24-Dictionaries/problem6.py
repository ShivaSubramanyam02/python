employees = {
    "emp1": {"name": "John", "department": "HR"},
    "emp2": {"name": "Emma", "department": "IT"},
    "emp3": {"name": "Harry", "department": "Finance"}
}
for key,value in employees.items():
    print(f"{value['name']}works in {value['department']} department")