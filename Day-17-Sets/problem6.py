set_a = {"apple", "banana", "cherry"}
set_b = {"cherry", "date", "fig"}

jk = set_a.union(set_b)
rk = set_a.intersection(set_b)
set_a -= rk
print(set_a)

