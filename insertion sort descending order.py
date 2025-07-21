a=[1,3,7,2,4,9]
n=len(a)

for i in range(1,n):
    j=i
    while  j > 0 and a[j-1]<a[j]:  #j=1,     a[1-1=0]=1>a[1]=3         2
        a[j],a[j-1]=a[j-1],a[j]
        j-=1
print(*a)


#[1,3,7,2,4,9]


