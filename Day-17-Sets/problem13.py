numbers = set(range(1, 11))  
for num in list(numbers):
    if num%3==0:
        numbers.remove(num)
        
numbers.add(11)
numbers.add(12)
print(numbers)

        