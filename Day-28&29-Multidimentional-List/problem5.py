items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

left_diagonal = []

right_diagonal = []

for i in range(len(items)):
    left_diagonal.append(items[i][i])
    right_diagonal.append(items[i][len(items) - 1 - i]) 
    
print("Left Diagonal:", left_diagonal)
print("Right Diagonal:", right_diagonal)