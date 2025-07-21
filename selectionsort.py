a=[1,3,7,2,4,9]
n=len(a)

for i in range(0,n-1):
    curr=i
    for j in range(i+1,n):
        if a[j]<a[curr]:
            curr=j
    a[j],a[curr]=a[curr],a[j]
print(a)
            