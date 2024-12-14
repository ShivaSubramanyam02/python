#1
jump = 1
meter = 0
while jump<=100:
    print("JUMP")
    jump+=1
    meter = meter + 1
print(meter,"times")


#2
guests = 5
count = 0
while count < guests:
    print("welcome guests!")
    count +=1
    
#3
num = 1
while num<=50:
    print(num)
    num+=2
    
    
#4
num = 3
while num<=20:
    print(num)
    num+=3
    

#5
num = 2
count = 0
total_sum = 0
while num<=100:
    print(num)
    num+=2
    count = count+1
    total_sum += num
    
avg = total_sum / count
print(avg,"average")




#6
num = 11
count = 0
while num>0:
    num-=1
    count+=1
    print(num)
    

    
#7
num = int(input("enter any number:"))
i = 1
while i<=10:
    i +=1
    print(num*i)
    
    
