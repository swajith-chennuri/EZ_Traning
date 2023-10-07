def OTP(a):
    b=[int(a[x])**2 for x in range(len(a)) if  x%2!=0]
    print(b)
    c=''.join(str(x) for x in b)
    d=c[:4]
    print(d)
a=input()
OTP(a)