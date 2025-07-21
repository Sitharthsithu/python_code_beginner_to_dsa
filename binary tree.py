a=[1,2,3,4,5,6,8,7,9,0]
n=len(a)
max=0
for i in range (0,n):
    for j in range (i+1,n):
        sum=0
        for k in (a[i:j]):
            sum+=k
        if sum>max: #5>0
            max=sum
print(max)