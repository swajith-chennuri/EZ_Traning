c=input()
l=[x for x in c]
b=[]
a=0
for i in range(len(l)):
    if l[i]=="{" or l[i]=="[" or l[i]=="(":
        b.append(l[i])
    elif l[i]=="}" or l[i]=="]" or l[i]==")" :
        if len(b)!=0:
            if l[i]=="}" and b[len(b)-1]=="{":
                b.pop()
            elif l[i]=="]" and b[len(b)-1]=="[":
                b.pop()
            elif l[i]==")" and b[len(b)-1]=="(":
                b.pop()
            else:
                print("balance is missing at :",i+1)
                a=1
                break
        else:
            print("balance is missing at :",i+1)
            a=1
            break
if len(b)==1 and a==0:
    print("balance is missing at :",len(l)+1)
elif len(b)>1 and a==0:
    print("balance is missing at :",len(l)-len(b)+1)
elif len(b)==0 and a==0:
    print("balanced")