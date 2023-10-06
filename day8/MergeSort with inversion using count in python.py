# MergeSort
def mergeSort(array):
    global c
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
                
            else:
                array[k] = M[j]
                c+=len(L)-i
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
array =list(map(int,input("enter a list = ").split(" ")))
c=0
mergeSort(array)
print("Sorted array is: ")
printList(array)
print(c)