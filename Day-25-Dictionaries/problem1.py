sentence = "hello world hello"

words = sentence.split()

empty_dictionary = {}

for word in words:
    if word in empty_dictionary:
        empty_dictionary[word] += 1
    else:
        empty_dictionary[word] = 1
        

print(empty_dictionary)