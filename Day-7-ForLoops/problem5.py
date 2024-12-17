sum = 0
count = 0
for x in range(1,101,1):
    if x%2==0:
        print(x)
    count = count + 1
    sum = sum + x
    avg = sum / count
print(avg)

    
  