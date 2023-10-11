def sub_array(arr,k):
    maximum_sum=sum(arr[:k])
    prev_sum=maximum_sum
    i=1
    j=k
    while j<len(arr):
        current_sum=prev_sum-arr[i-1]+arr[j]
        i+=1
        j+=1
        prev_sum=current_sum
        maximum_sum=max(maximum_sum,current_sum)
    return maximum_sum
def max_sum(arr):
    max_sum=0
    for i in range(len(arr)):
        current=sub_array(arr,i)
        max_sum=max(max_sum,current)
    return max_sum
arr=[-1,2,5,-12,1,4,4,10]
print(max_sum(arr))
