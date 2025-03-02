def is_prime(num):
    count = 0
    for x in range(1, num + 1):
        if num % x == 0:
            count += 1
    return count == 2

num = int(input("Enter a number:"))
if is_prime(num):
    print(f"{num} - it is a PRIME number")
else:
    print(f"{num} - NOT A PRIME")
