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
arr=[1,2,5,112,1,4,4,10]
k=3
print(sub_array(arr,k))
