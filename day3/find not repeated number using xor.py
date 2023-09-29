a=list(map(int,input().split(" ")))
def find(ar,n):
    result=ar[0];
    for i in range(1,n):
        result=result^ar[i]
        return result
print(find(a,len(a)))

