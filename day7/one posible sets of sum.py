def sets(a,n,target):
    for i in range(n):
        b=[]
        for j in range(i):
            if a[j] not in b:
                b.append(a[j])
                if sum(b)==target:
                    print(b)
a=[8,6,5,4,3,2,26]
sum_input=int(input())
if sum_input>sum(a) or sum_input<min(a):
    print("impossible")
elif sum_input==sum(a):
    print("only one set is possible i.e ",a)
else:
    for i in range(len(a)):
        if a[i]>sum_input:
            a.pop(i)
    print(sets(sorted(a),len(a),sum_input))
