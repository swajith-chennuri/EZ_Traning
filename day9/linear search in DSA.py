def linear_search(list1,key):
    for i in range(len(list1)):
        if list1[i]==key:
            print("key find at index of :",i)
list1=list(map(int,input().split()))
key=int(input())
linear_search(list1,key)