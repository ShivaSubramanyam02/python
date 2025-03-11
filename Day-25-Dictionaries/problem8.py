string = "mississippi"

words = string

empty = {
}

for word in words:
    if word in empty:
        empty[word] += 1
    else:
        empty[word] = 1
        
print(empty)