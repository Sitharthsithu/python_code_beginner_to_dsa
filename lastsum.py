s=str(input("Enter the String :"))
n=len(s)
a=[]
if a[::-1]==a:    
    for i in range(n):
        for j in range(i, n):
            a.append(s[i:j+1])
    print(a)

else:
    print(list(s))
    
        
