def factorial(a):
    fact = 1
    for x in range(1,a+1):
        fact = fact * x
    return fact
    
print(factorial(5))