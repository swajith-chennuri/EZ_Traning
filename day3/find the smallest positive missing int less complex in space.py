a=list(map(int,input().split(" ")))
print(a)
for i in range(len(a)):
    if i not in a:
        print(i)
        break;