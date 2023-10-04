def bubble_sort(a):
    for j in range(0,len(a)-1):
        c=0
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                c=1
        if c==0:
            break
    return a
a = list(map(int,input("enter a list = ").split(" ")))
print(bubble_sort(a))