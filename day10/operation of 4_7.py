a=input()
list1=a.split(',')
b=list1.index('4')
c=list1.index('7')
mtl=list1[:b-1]+list1[c+1:]#empty list
mtl=[int(i) for i in mtl ]
mtl1=list1[b:c+1]
print("sum of numers not b/w 4,7 in string :",sum((mtl)))
d=int(''.join(mtl1))
print("string of 4_7 : ",d)
print("sum of all : ",sum(mtl)+d)
