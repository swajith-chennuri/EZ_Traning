array =list(map(int,input("enter a list = ").split(" ")))
c=0
for i in range(len(array)):
    for j in range(i+1,len(array),1):
        if i<j:
            if array[i]>array[j]:
                c+=1
                array[i],array[j]=array[j],array[i]   
print(c)
print(array)