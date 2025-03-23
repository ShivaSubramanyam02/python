items = [
    [2, 7, 6],
    [3, 4, 9],
    [8, 5, 10]
]

count = 0

for row in items :
    for num in row:
        if num%2==0:
            count+=1
print("The Count of Even Numbers:", count)