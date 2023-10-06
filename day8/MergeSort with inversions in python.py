def merge_sort_with_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, right_half = arr[:mid], arr[mid:]

    left_half, left_count = merge_sort_with_inversions(left_half)
    right_half, right_count = merge_sort_with_inversions(right_half)

    merged = []
    i = j = 0
    count = left_count + right_count
    inversion_count = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
            inversion_count += len(left_half) - i

    merged.extend(left_half[i:])
    merged.extend(right_half[j:])

    return merged, count + inversion_count

# Input
array = list(map(int, input("Enter a list of integers: ").split()))

# Call merge_sort_with_inversions to sort the input list and count inversions
sorted_arr, inversions = merge_sort_with_inversions(array)

# Output the sorted array and the number of inversions
print("Sorted array is:", sorted_arr)
print("Number of inversions:", inversions)
