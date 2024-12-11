#1
num = int(input("enter a number:"))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("zero")
    
    
#2
num = int(input("enter a number:"))
if num<18:
    print("you are not adult")
elif num>18:
    print("you are adult")
else:
    print("invalid number")

#3
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))
if num1>=num2 and num1>=num3:
    print("num1")
elif num2>=num1 and num2>=num3:
    print(num)
else:
    print(num3)
    
    
#4
temperature = int(input("Enter then temperature: "))
if temperature == 30:
    print("Normal temparature")
elif temperature > 30:
    print("too hot")
elif temperature < 20:
    print("too cold ")

    
#5
num = int(input("enter a number"))
if num % 2==0:
    print("Even number")
else:
    print("odd number")

#6
P = int(input("enter your marks"))
if P >= 85:
    print("A")
elif P>=75:
    print("b")
elif P>=65:
    print("C")
else:
    print("F THATS SAD BRO")



#7
year = int(input("enter year:"))
if year%400==0:
    print("leap year")
else:
    print("not a leap year")
    
#8
angle1 = int(input("Enter your number"))
angle2 = int(input("Enter your number"))
angle3 = int(input("Enter your number"))
sum = angle1 + angle2 + angle3
if sum==180:
    print("Valid triangle")
elif sum==90:
    print("right angle triangle")
else:
    print("Invalid shape")
    
    
#9
P = float(input("Enter your number"))
I = float(input("Enter your number"))
T = float(input("Enter your number"))
formulae = (P*I*T) / 100
print(formulae)



#10
A = float(input("Enter your number"))
B = float(input("Enter your number"))
if A%B==0:
    print("Divisible")
elif A%B!=0:
    print("Not Divisible")
else:
    print("invalid")

