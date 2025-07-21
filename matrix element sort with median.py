#3
#3
#1 3 5 
#2 6 9 
#3 6 9

d=int(input())
b=int(input())
a=[]
c=[]
for i in range(d):
    d=list(map(int,input().split()))
    a.append(d)

for i in range(d):
    for j in range(b):
        c.append(a[i][j])
print(c)
for i in range(len(c)-1):
    j=i
    while j>0 and c[j+1]<c[j]:
        c[j],c[j+1]=c[j+1],c[j]
        j-=1
print(c)

low=0
high=len(c)
mid=int((low+high)/2)

print(c[mid])