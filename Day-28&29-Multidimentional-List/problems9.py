items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


border_sum = sum(items[0]) + sum(items[-1])

border_sum += items[1][0] + items[1][2]

print(border_sum)
    