set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date", "fig"}
intersection = set_a.intersection(set_b)
set_b -= intersection
print(set_b)