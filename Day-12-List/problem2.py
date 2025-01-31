numbers = [10, 5, 8, 12, 3]
max_number = numbers[0]
min_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num
print(max_number)
print(min_number)
    