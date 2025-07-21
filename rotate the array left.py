a=[1,2,3,4,5,6,7]
n=3
c=[]
for i in range(len(a)):
    if(n>i): 
        c.append(a[i])
print(c)
for i in c:
    d=a.remove(i)
print(a)

print(a+c)


#for i in c:
#    e=a.append(i)
#print(a)