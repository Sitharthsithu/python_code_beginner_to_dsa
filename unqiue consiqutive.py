a=int(input())#a=5
c=input().split()#c=['a','b','a','c','d']
d,e=1,4
f=[]
for i in range(d,e):
    if c[i] not in f:
        f.append(c[i])
        
print(len(f))# is 3 