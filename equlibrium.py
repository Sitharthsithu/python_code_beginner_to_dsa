def func(arr):#equilabrium sum
    total=sum(arr)
    left=0
    for i in range(len(arr)):
        if left==total-left-arr[i]:
            return arr[i],i
        left+=arr[i]
arr=[-7, 1, 5, 2, -4, 3, 0]
print(func(arr))