def query_subarray_sum(arr,query_arr):
    n=len(arr)
    prefix_sum=[0]*n
    for i in range(n):
        prefix_sum[i]=arr[i]+prefix_sum[i-1]
    for query in query_arr:
        i=query[0]
        j=query[1]
        if i==0:
            print(prefix_sum[j],end=' ')
        else:
            print(prefix_sum[j]-prefix_sum[i-1],end=' ')
arr=[-3,8,7,2,-5,13,18,9,6]
query_arr=[[1,4],[2,6],[4,6],[2,7]]
query_subarray_sum(arr,query_arr)