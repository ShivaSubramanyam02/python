quantities = [2, 3, 5, 1]
prices = [50, 30, 20, 10]

total = 0
for i  in range(len(quantities)):
    total += quantities[i] * prices[i]

print(total)
    