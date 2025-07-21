def binary_search(a, target):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
        return -1

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                
a=[1,3,5,6]
target=7

for i in a:
  if i==target:
    print(binary_search(a,target))
  else:
      d=a+[target]
e=bubble_sort(d)
print(binary_search(e,7))
      #print(binary_search(e,target))
      
      
      