even_numbers = {2, 4, 6, 8, 10}
prime_numbers = {2, 3, 5, 7}
jk = even_numbers.intersection(prime_numbers)
even_numbers -= jk
print(even_numbers)
