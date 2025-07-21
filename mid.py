k=6
a=[12,-3,14,-56,77,13]
c=[]
for i in a:
    if i>0:
        c.append(i)
n=len(c)
#left=c[0]
#right=c[-1]

#mid=(left+right)//2

#print(mid)
if n == 0:
    print("nil")
elif n % 2==1:
    new = c[n//2]
else:
    new=(c[n//2-1] + c[n//2])/2
print("Median is: ",new)