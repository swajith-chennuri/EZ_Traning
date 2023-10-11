'''Sum of first n positive integers = n(n + 1)/2, where n is the total number of integers. Let us see the applications of the sum of integers formula along with a few solved examples.'''
#find the missing element from given array
n=10
arr=[1,8,4,3,5,2,6,10,9]
for i in range(1,n):
    if i not in arr:
        print(i,"is missing in array")
sum=n*(n+1)//2
print(sum-sum(arr))
