numbers = (10, 15, 20, 25, 30, 35, 40)
empty_tuple = ()
for num in numbers:
    if num % 20 == 0:
        empty_tuple += (num,)
        
print(empty_tuple)
        
        



