for i in range(1, 7+1):
    count=0
    for j in range(i): 
        if j==0 or j == i-1 or j==7:
            print(chr(65+count),end=" ")
            count+=1
            
        else:
            print("",end=" ")
            
    print()
    