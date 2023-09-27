def mon_intrest(account_balance):
    monthly_intrest=account_balance/100
    return monthly_intrest;
account_balance=int(input("enter 1st balance = "));
c=int(input("enter withdraw ammount = "));
d=int(input("enter month number = "));
b=account_balance-c;
e=int(input("enter deposit ammount = "));
f=int(input("enter month number = "));
g=b+e;
print(g+(mon_intrest(account_balance)*(d-1))+(mon_intrest(b)*(f-d))+(mon_intrest(g)*(13-f)))
