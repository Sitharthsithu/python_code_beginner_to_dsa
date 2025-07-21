a = [-5, 3, 7, -2, 9, 4, -1]
b=[]
i=0
c=0
for i in range(len(a)):
    if a[i]>0:
        b.append(a[i]) 
        c= c+a[i] # mean
b.sort()
print(b)

n=len(b)
d = c/n
print("mean is: " ,d)

if n == 0:
    print("nil")
elif n % 2==1:
    new = b[n//2]
else:
    new=(b[n//2-1] + b[n//2])/2
print("Median is: ",new)