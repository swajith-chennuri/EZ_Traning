def max_sub_array(a):
    maximum_sum = float("-inf")
    current_sum = a[0]
    n=len(a)
    for i in range(1,n):
        if current_sum < 0:
            current_sum = 0
        if a[i] < 0:
            maximum_sum=max(maximum_sum,current_sum)
        current_sum = current_sum+a[i]
    return max(maximum_sum,current_sum)
arr = [4, -10, -2, 85,56,-100,120]
result = max_sub_array(arr)
print(result)
