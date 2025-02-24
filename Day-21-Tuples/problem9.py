nested = (('a', 'b'), ('c', 'd'), ('e', 'f'))
second  = tuple(item[1] for item in nested)
print(second)