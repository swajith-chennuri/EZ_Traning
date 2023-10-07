a=input()
list1=a.split(',')
print("index for 4 : ",list1.index('4'))
print("index for 4 : ",list1.index('7'))
mtl=[]#empty list
mtl1=[]
for i in range(list1.index('4')):
    mtl.append(int(list1[i]))
for i in range(list1.index('7')+1,len(list1)):
    mtl.append(int(list1[i]))
for i in range(list1.index('4'),list1.index('7')+1):
    mtl1.append(list1[i])
print("sum of numers not b/w 4,7 in string :",sum(mtl))
b=int(''.join(mtl1))
print("string of 4_7 : ",b)
print("sum of all : ",sum(mtl)+b)