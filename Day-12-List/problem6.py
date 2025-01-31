numbers = [4, -3, 7, -1, 0, 5]
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print(numbers)