a=int(input())
s=["{","}","[","]","(",")"]
if a%2!=0:
        print("not posible to balance")
else:
    for i in range(a):
        print(s[i%6],end=" ")