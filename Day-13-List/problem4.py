list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
empty_list = []
for x in list1:
    if x in list2:
        empty_list.append(x)
        
print(empty_list)