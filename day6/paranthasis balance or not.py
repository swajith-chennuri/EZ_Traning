l=[]
b=[]
n=int(input("enter the no of elements = "))
c,o,a=0
if n%2!=0:
    a=1
else:
    for i in range(n):
        l.append(input("enter the element = "))
    print(l)
    for i in range(n):
        if l[i]=="{" or l[i]=="[" or l[i]=="(":
            o=o+1
        else:
            c=c+1
    if(c!=o):
        a=1
    else:
        for i in range(n):
            if l[i]=="{" or l[i]=="[" or l[i]=="(":
                b.append(l[i])
            elif l[i]=="}" or l[i]=="]" or l[i]==")" :
                if l[i]=="}" and b[len(b)-1]=="{":
                    b.pop()
                elif l[i]=="]" and b[len(b)-1]=="[":
                    b.pop()
                elif l[i]==")" and b[len(b)-1]=="(":
                    b.pop()
                else:
                    a=1
                    break
if a==0:
    print("balanced")
else:
    print("imbalanced")