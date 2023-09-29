# after create an array find the smallest positive integer in array
a=list(map(int,input().split(" ")))
b=[]
for i in range(len(a)):
    if a[i]>=0:
        b.append(a[i])
b=sorted(b)
print(b[0])