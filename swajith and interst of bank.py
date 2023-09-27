def intrest(a):
    monthly_intrest=a/100
    return monthly_intrest;
a=int(input("enter ammount in bank = "));
b=a-int(input("enter withdraw ammount = "));
c=b+int(input("enter diposit ammount = "));
print("balnce =",c+(intrest(a)*4)+(intrest(b)*4)+(intrest(c)*4))