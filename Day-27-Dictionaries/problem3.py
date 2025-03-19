words_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

epmty = {}

for word in words_list:
    if word in epmty:
        epmty[word] += 1
    else:
        epmty[word] = 1
        
print(epmty)
        
        