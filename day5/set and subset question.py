def a(arr,n,target):
    if target == 0:
        return True
    if n==0 and target!=0:
        return False
    if arr[n-1]>target:
        return a(arr,n-1,target)
    return a(arr,n-1,target) or a(arr,n-1,target-arr[n-1])
arr = list(map(int,input().split(" ")))
target= int(input())
n = len(arr)
if a(arr, n, target):
    print("True")
else:
    print("False")
        