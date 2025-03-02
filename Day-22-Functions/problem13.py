def count_vowels(a):
    vowels = 'aeiou'
    count = 0
    for char in a:
        if char in vowels:
            count+=1
    return count


print(count_vowels("hello"))
    