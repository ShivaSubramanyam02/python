for x in range(5,0,-1):
    for y in range(5-x):
        print(" ",end="")
    for z in range(x):
        print("*",end="")
    print()