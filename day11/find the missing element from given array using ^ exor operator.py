'''Sum of first n positive integers = n(n + 1)/2, where n is the total number of integers. Let us see the applications of the sum of integers formula along with a few solved examples.'''
#find the missing element from given array
def exor(arr,n):
    ans=0
    for i in range(1,10+1):
        ans=ans^i
    for i in range(n-1):
        ans=ans^arr[i]
    return ans
n=10
arr=[1,8,4,3,5,2,6,10,9]
print(exor(arr,n))