a=[1,2,3,4,5]
d=[]
for i in range(1,len(a)):
    if i == 1:
        c=a[i-1]+a[i]
        print(c)
        a.pop(0)
        a.pop(0)
        print(a)
        d.append()
    