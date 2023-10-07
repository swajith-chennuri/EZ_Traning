#count sort
def count(list1):
    length=len(list1)
    maximum=max(list1)
    list2=[0]*(maximum+1)
    list3=[0]*(length)
    for i in list1:
        list2[i]+=1
    print("count array : ",list2)
    for i in range(1,maximum+1):
        list2[i]=list2[i-1]+list2[i]
    print("cumulative sum of array : ",list2)
    for i in range(1,maximum+1):
        for z in range(list2[i-1],list2[i]):
            list3[z]=i
    print("sorted array : ",list3)
list1=list(map(int,input().split()))
count(list1)