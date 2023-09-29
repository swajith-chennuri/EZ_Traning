#python
b=input()
a=[int(x) for x in b.split(" ")]
print(a)
for i in range(len(a)):
    if i not in a:
        print(i)
        break;