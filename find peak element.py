a=[10,20,15,2,23,90,80]
for i in range(1,len(a)):
    if(a[i-1]<a[i])and(a[i]>a[i+1]):
        print(i,end=" ")