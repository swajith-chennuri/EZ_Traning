l=[]
n=int(input("enter the no of elements = "))
for i in range(n):
    l.append(input("enter the element = "))
print(l)
for i in range(n):
    print(l.pop(0))
print(l)
