
count = 0
num = int(input("Enter a number:"))

for x in range(1,num+1):
    if num%x==0:
        count+=1
        
if count==2:
    print(f"{num} - it is a PRIME number")
else:
    print(f"{num} - NOT A PRIME")
        
            

        
