items = [
    [5, 2, 3],
    [4, 5, 6],
    [7, 8, 5]
]

count = 0


for num in items:
    for y in num:
        if y==5:
            count+=1
            
print("Number of times 5 appears:", count)