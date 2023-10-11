def is_pair_exist(arr,target):
    a=0
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)-1):
            if arr[i]+arr[j]==target:
                print( arr[i],arr[j])
                a+=1
                break
    if a==0:
        print("pair not exist")
arr=[-3,8,7,2,-5,13,18,9,6]
target=20
is_pair_exist(arr,target)
