def bubble_sort(a):
    for j in range(0,len(a)-1):
        c=0
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                c=1
        if c==0:
            break
    return a
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        print(array)
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
        print(array)
    return array
def selectionSort(a):
    size=len(a)
    for step in range(size):
        min_i = step
        for i in range(step + 1, size):
            if a[i] < a[min_i]:
                min_i = i
        (a[step],a[min_i]) = (a[min_i], a[step])
    return a
a = list(map(int,input("enter a list = ").split(" ")))
b=a
print('Sorted Array in Ascending Order:')
print("bubble sort \n",bubble_sort(a))
a=b
print(insertionSort(a))
a=b
print(selectionSort(a))
