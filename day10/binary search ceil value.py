def binary_search_ceil(arr,target):
    left,right = 0,len(arr) -1
    while left<= right:
        mid = left+(right-left)
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            ceil = arr[mid]
            right = mid -1
    return ceil
print(binary_search_ceil([1,2,3,8,9,12,13],7))