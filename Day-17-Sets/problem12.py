words = {"python", "java", "c++", "ruby", "javascript"}
for word in list(words):
    if "a" in word:
        words.remove(word)
words.add("swift")
print(words)