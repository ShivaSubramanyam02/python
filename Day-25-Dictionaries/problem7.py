original_dict = {'a': 1, 'b': 2, 'c': 3}

empty_dict = {}

for key,value in original_dict.items():
    empty_dict[value] = key
    
    
print(empty_dict)