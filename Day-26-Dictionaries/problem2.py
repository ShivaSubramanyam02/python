data = {'item1': 45, 'item2': 22, 'item3': 78, 'item4': 33}

max_key = max(data, key=data.get)
min_key = min(data, key=data.get)


print(f"Maximum value: {data[max_key]}, Key: '{max_key}'")
print(f"Minimum value: {data[min_key]}, Key: '{min_key}'")
