#Comprehensive Inventory Analysis
A = 12.50
Q1 = 20
B = 7.30
Q2 = 15
C = 5.25
Q3 = 10
Pro1 = A*Q1
Pro2 = B*Q2
Pro3 = C*Q3
print(f"Total value of Product A:${Pro1}")
print(f"Total value of Product B:${Pro2}")
print(f"Total value of Product C:${Pro3}")
sum = Pro1+Pro2+Pro3
print(f"Sum of total values:${sum}")
diff = Pro1 - Pro2
print(f"Difference between highest and second highest value product:{diff}")
product = Q1*Q2*Q3
print(f"Product of total values:{product}")
average_quantity = Q1+Q2+Q3
avg = average_quantity / 3
print(f"Average quantity:{avg}")
total = Q1+Q2+Q3
Avg = sum % total
print(f"Average price per unit:${Avg}")
remainder = (Q1 + Q2+ Q3) % 6
print(f"Remainder of total quantity divided by 6:{remainder}")
square = (B*C) ** 0.5
print(f"Square root of product of total values of B and C:{square}")
print("Concatenated product info: Product A: 20 at $12.50 each, Product B: 15 at $7.30 each, Product C: 10 at $5.25 each")
