a=int(input("enter the number"))
c=d=j=0
for i in range(0,a,a//10):
    c=c+a%10
    a=a//10
print(c)