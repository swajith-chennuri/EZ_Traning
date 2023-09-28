matrix = [[0 for j in range(3)] for i in range(3)]
matrix[0][0]=1
matrix[0][1]=2
matrix[0][2]=3
matrix[1][0]=4
matrix[1][1]=5
matrix[1][2]=6
matrix[2][0]=7
matrix[2][1]=8
matrix[2][2]=9
print("clock wise rotation")
for i in range(3):
    for j in range(3-1,-1,-1):
        print(matrix[j][i], end=" ")
    print()
print("anti_clock wise rotation")
for i in range(3-1,-1,-1):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()