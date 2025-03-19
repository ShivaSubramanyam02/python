string = "hello world"
vowels = "aeiou"
vowel_count = {}

for v in vowels:
    vowel_count[v] = string.lower().count(v)

print(vowel_count)
