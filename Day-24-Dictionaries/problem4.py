numbers = {
    "a": 10,
    "b": 15,
    "c": 5,
    "d": 20
}
threshold = 12

filtered_numbers = {}

for key,value in numbers.items():
    if value <= threshold:
        filtered_numbers[key] = value
        
print(filtered_numbers)

    