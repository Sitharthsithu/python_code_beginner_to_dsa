n=5
a=[1,2,3,4,5]
d,e=1,4
i = d #1
j = e - 1  #4-1=3 
while i < j: #1<3 true so loop iterate
    a[i], a[j] = a[j], a[i] #2,4 =[1,4,3,2,5]
    i += 1 #1+1=2
    j -= 1 #3-1=2

print(a)
    