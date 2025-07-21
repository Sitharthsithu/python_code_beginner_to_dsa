a=[0,5,4,0,6,0,1,0,8,9]
zeros=[]
non_zeros=[]

for x in a:
    if x == 0:
        zeros.append(x)
        
for x in a:
    if x != 0:
        non_zeros.append(x)

result = zeros + non_zeros
print(result)

