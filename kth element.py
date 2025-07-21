
a=[1,2,3,5,6]
first=float('inf')
second=float('inf')
for i in range(len(a)):
    if a[i]<first:
        second=first
        first=a[i]
    elif a[i]<second and a[i]!=first:
        second=a[i]
if second==float('inf'):
    print('No element')
else:
    print(second)