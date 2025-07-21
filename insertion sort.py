a=[1,3,7,2,4,9,9,3]
n=len(a)

for j in range(n):
    while j>0 and a[j-1]>a[j]:  #j=1,     a[1-1=0]=1>a[1]=3         
        a[j],a[j-1]=a[j-1],a[j]
        j-=1
print(*a)
    

#[1,3,7,2,4,9]

