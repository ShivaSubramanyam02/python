#1
Year = int(input("Enter your Year: "))
Pyear = 2024
age = Pyear - Year
print(age)
if age>=13 and age<=19:
    print("teenage")
elif age>=20 and age<=29:
    print("twenties")
else:
    print("error")
    

#2
J = input("enter a word : ")
C = ("aeiou")
if J in C and len(J)==1:
    print("Vowlel!")
else:
    print("not a vowel")
    


#3
a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif a == b == c:
    print("TRUCEE")
else:
    print(c)


#4
family_member = True
Invitation_card = True
if Invitation_card or family_member:
    print("ALLOW ENTRY")
else:
    print("NO ENTRY")