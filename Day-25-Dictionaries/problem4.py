students = {
    "Alice": ["Math", "Science"],
    "Bob": ["English"],
    "Charlie": ["History", "Math"]
}
new_subject = "Physical Education"

for key,value in students.items():
    value.append(new_subject)
    
print(students)