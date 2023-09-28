a=int(input())
for i in range (0,a,1):
    for j in range (0,i,1):
        print("*",end=" ")
    print()
for i in range (a,0,-1):
    for j in range (0,i,1):
        print("*",end=" ")
    print()
a=int(input())
for i in range (0,a,1):
    print("*"*i)
a=int(input())
for i in range (0,a,1):
    for j in range (0,a-i):
        print(" ",end=" ")
    for k in range (0,i+1):
        print("*",end=" ")
    print()
a=int(input())
for i in range (0,a,1):
    for j in range (0,a-i):
        print(" ",end=" ")
    for j in range (0,i,1):
        print("*",end=" ")
    for k in range (0,i+1):
        print("*",end=" ")
    print()  