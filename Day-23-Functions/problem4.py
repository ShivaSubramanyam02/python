def list_of_squares(n):
    result = []
    
    for i in range(1,n+1):
        result.append(i**2)
        
    return result

print(list_of_squares(5))