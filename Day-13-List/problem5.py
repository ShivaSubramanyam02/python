numbers = [1, 2, 3, 2, 4, 5, 3, 6, 5]
empty_list = []
for num in numbers:
    if num not in empty_list:
        empty_list.append(num)
print(empty_list)