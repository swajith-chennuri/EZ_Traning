# for the given numer n check the kth bit is set or not
n=int(input())
k=int(input())
if n&(1<<k-1)==0:
    print("not set")
else:
    print("set")
