students_in_classA = {"Alice", "Bob", "Charlie", "David"}
students_in_classB = {"Eve", "Frank", "Charlie", "Bob"}

jjk = students_in_classA.intersection(students_in_classB)
students_in_classA -= jjk
print(students_in_classA)