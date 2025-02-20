numbers = (1, 2, 3, 2, 4, 2, 5)
count = 0
target = 2
for num in numbers:
    if target == num:
        count+=1
print(f"target appeared = {target} , {count} =times")

