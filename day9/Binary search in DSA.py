def binary_search(list1,key):
    low=0
    high=len(list1)-1
    while low<=high:
        mid=(low+high)//2
        if list1[mid]==key:
            return mid
        elif key<list1[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
list1=list(map(int,input("enter the list :").split()))
key=int(input("enter the target you want to find :"))
return_value=binary_search(list1,key)
if return_value!=-1:
    print("key find at index of :",return_value)
else:
    print("element not found!")
    