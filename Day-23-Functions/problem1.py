def count_consonants(n):
    count = 0
    consonants = 'bcdfghjklmnpqrstwxyz'
    
    
    for letters in n:
        if letters in consonants:
            count+=1
    return count
    
    
    
print(count_consonants("hello"))
            
            
            