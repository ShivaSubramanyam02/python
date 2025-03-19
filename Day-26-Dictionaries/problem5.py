list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]

unique_dict = {}
for item in list_with_duplicates:
    unique_dict[item] = None

unique_list = list(unique_dict)

print(unique_list)
