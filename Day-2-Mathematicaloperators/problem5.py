#Advanced Inventory Calculations
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
diff = (Pro1-Pro3)
print(f"Difference between highest and lowest value product:${diff}")
product = Pro1*Pro2*Pro3
print(f"Product of total values:{product}")
average_quantity = Q1+Q2+Q3
avg = average_quantity / 3
print(f"Average quantity:{avg}")
Mod = Q1+Q2+Q3
mod = Mod % 7
print(f"Remainder of total quantity divided by 7:{mod}")
square = 412.00 ** 0.5
print(f"Square root of sum of total values:{square}")
print("Concatenated product info: Product A: $250.00, Product B: $109.50, Product C: $52.50")