a=[]
b=int(input("enter the range "))
while(len(a)!=b):
    c=int(input("enter the number ="))
    if c<=40 and c>10:
        a.append(c)
    else:
        print("enter the values between 10-35")
print("even")
for i in range(len(a)):
    if a[i]%2==0:
        print(a[i],end=" ")
print()
print("sqare of 2")
for i in range(len(a)):
    if a[i]&a[i]-1== 0 :
        print(a[i],end=" ")