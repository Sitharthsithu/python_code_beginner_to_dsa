s="saaaaaaaaaaasbbbbbbbbss"
n=len(s)
c=""
a=[]    
for i in range(n):
    for j in range(i, n):
        a.append(s[i:j+1])
        
        if len(a[::-1])>len(a):
            c=a[::-1]

