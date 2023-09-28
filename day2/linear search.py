def sumof(arr,b):
    for i in range(len(arr)):
        if(arr[i]==b):
            print("element found at index of ",i)
        break;
a=list(map(int,input().split(" ")))
b=int(input("enter the element to search"))
sumof(a,b) 