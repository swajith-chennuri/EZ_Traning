a=input()
index=0
b=[]
sp=""
for i in range(len(a)):
    if not a[i].isalpha():
        sp=a[i]
        index=i
    else:
        b.append(a[i])
f=b[::-1]
f.insert(index,sp)
print(''.join(f))