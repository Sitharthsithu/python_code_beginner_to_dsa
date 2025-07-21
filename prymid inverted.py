for i in range(7):
    for j in range(i):
        print(" ",end="")
    for j in range(7,i,-1):
        print("",chr(72-j),end="")
    print()

