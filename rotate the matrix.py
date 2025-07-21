a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

n=len(a)
for i in range(0,n):
    for j in range(i+1,n):
        a[i][j],a[j][i]=a[j][i],a[i][j]
        #i=0
        #a[0][1],a[1][0]==2,4
        #a[0][2],a[2][0]==3,7
        #i=1
        #a[1][2],a[2][1]==5,8
        

print(a)

for r in a:
    r.reverse()
print(a)

#[[7, 4, 1],
#[8, 5, 2],
#[9, 6, 3]]