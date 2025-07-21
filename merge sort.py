def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    mid = len(arr) // 2  # Divide the array
    left_half = merge_sort(arr[:mid])   # Sort left half
    right_half = merge_sort(arr[mid:])  # Sort right half

    return merge(left_half, right_half)  # Merge them


def merge(left, right):
    sorted_arr = []
    i = j = 0  # Pointers for left and right

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # If any elements left
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

arr = [6, 3, 9, 5, 2, 8]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

