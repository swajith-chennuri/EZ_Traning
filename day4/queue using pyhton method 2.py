from collections import deque
l=deque()
n=int(input("enter the no of elements = "))
for i in range(n):
    l.append(input("enter the element = "))
print(l)
for i in range(n):
    print(l.popleft())
print(l)