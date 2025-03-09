student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88,
    "Diana": 95
}

temp = max(student_scores,key=student_scores.get)
print(temp,student_scores[temp])


