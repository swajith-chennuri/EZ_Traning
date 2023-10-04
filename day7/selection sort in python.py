def selectionSort(a,size):
    for step in range(size):
        min_i = step
        for i in range(step + 1, size):
            if a[i] < a[min_i]:
                min_i = i
        (a[step],a[min_i]) = (a[min_i], a[step])
a =list(map(int,input("enter a list = ").split(" ")))
size = len(a)
selectionSort(a, size)
print('Sorted Array in Ascending Order:')
print(a)