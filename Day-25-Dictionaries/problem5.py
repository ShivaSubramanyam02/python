dict1 = {'x': 1, 'y': 2, 'z': 3}
dict2 = {'w': 10, 'x': 11, 'y': 22}


common = list(dict1.keys() & dict2.keys())

print(common)