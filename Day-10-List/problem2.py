num = [10,2,35,65]
max_value = num[0]
min_value = num[0]
for n in num:
    if n > max_value:
        max_value = n
    if n < min_value:
        min_value = n
print("max-",max_value)
print("min-",min_value)

    