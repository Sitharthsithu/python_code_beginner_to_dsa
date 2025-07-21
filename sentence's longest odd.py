a="innate talent training institute"
b=a.split()
c=[]
for i in b:
    if len(i)%2==1:
        c.append(len(i))
print(max(c))
