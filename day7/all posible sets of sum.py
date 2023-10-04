def find_set(arr,n,target,current_sum,start,subset,res):
    if current_sum == target:
        res.append(subset[:])
        return
    if current_sum > target or start == n:
        return
    for i in range(start, n):
        subset.append(arr[i])
        current_sum += arr[i]
        find_set(arr,n,target,current_sum,i+1,subset,res)
        current_sum -= subset.pop()
def find(arr, target):
    n = len(arr)
    res= []
    find_set(arr,n,target,0,0,[],res)
    return res
a = list(map(int,input("enter a list = ").split(" ")))
sum_input=int(input("Enter the target sum: "))
if sum_input>sum(a) or sum_input<min(a):
    print("impossible")
elif sum_input==sum(a):
    print("only one set is possible, i.e.,", a)
else:
    filtered = [x for x in a if x<=sum_input]
    print("Possible sets:")
    sets = find(sorted(filtered), sum_input)
    for subset in sets:
        print(subset)