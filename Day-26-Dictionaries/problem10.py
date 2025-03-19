students = ['Alice', 'Bob']
ages = [20, 22]
subjects = [['Math', 'Science'], ['English', 'History']]

student_data = {}

for i in range(len(students)):
    student_data[students[i]] = {'age': ages[i], 'subjects': subjects[i]}
    

print(student_data)