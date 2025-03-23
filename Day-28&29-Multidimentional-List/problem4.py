items = [
    [10, 5, 8],
    [3, 7, 2],
    [6, 9, 4]
]

number_of_col = len(items[0])

for col in range(number_of_col):
    max_value = items[0][col]
    

    for row in items:
        if row[col] > max_value:
            max_value = row[col]

    print(max_value)

        
