numbers =  [1, 3, 7, 8, 3, 5, 3]
count = 0
target = 3
for num in numbers:
    if num == target:
        count+=1
    
print(f"{target}appears,{count}times")