a=[-5,3,7,-2,9,4,-1]
c=[]
for i in a:
    if i>0:
        c.append(i)
print(len(c))
n=len(c)
for i in range(n):
    for j in range(n-i-1):
        if(c[j]>c[j+1]):
            c[j],c[j+1]=c[j+1],c[j]
print(c)

if (len(c)%2==0):
    print(((n//2)+(n//2-1))/2)
else:
    print(n//2)