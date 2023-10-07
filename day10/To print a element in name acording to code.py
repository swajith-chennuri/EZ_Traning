b=input()
f=""
c=list(map(str,b.split(',')))
for i in range(len(c)):
    d=list(map(str,c[i].split(':')))
    e=sorted(d[1])
    h=0
    for j in range(len(d[1])):
        s=int(e[j])
        if s<=len(d[0]):
            h=int(e[j])
    g=d[0]
    if h<=len(g) and h>0:
        f+=g[h-1]
    else:
        f+="X"
print(f)