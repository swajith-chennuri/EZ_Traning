#count sort process
def count(list1,list2):
    list3=[]
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            a=list1[i]+list2[j]
            list3.append(a)
    list4=[0]*(max(list3)+1)
    c=0
    for i in list3:
        list4[i]+=1
    print("count array : ",list4)
    for i in range(len(list4)):
        if max(list4)==list4[i]:
            c=i
    return c
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
print(count(list1,list2))

