a=[7,1,5,3,6,4]
b=0
for i in range(0,len(a)):
    for j in range (i+1,len(a)):
        d=a[j]-a[i]
        b=max(d,b)
print(b)
        