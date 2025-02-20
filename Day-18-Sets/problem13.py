words = {"hello", "world", "python", "programming", "sets"}
for word in list(words):
    if len(word) > 5:
        words.remove(word)
        
words.add("code")
print(words)