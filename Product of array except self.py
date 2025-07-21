#Input: arr[] = [10, 3, 5, 6, 2]
#Output: [180, 600, 360, 300, 900]

#a=[10,3,5,6,2]
#b=[]
#for i in range(0,len(a)):
#    for j in range (0,len(a)):
#        if a[i]!=a[j]:
#                b.append(a[j])
#        if(len(b)==len(a)-1):
#            break
#    print(b)



a = [10, 3, 5, 6, 2]
c=[]
for i in range(len(a)):
    b = []  
    for j in range(len(a)):
        if i != j:
            b.append(a[j])
    
    #for i in b:
        #print(i*i+1)
    mul=1
    
    for i in b:
        mul*=i

    c.append(mul)
print(c)
    

