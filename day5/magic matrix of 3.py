def swajith(matrix):
    a=8
    b=1
    for i in range(n):
        for j in range(n):
            if (j!=1 and i!=1):
                matrix[i][j]=a
                a=a-2
            elif (j==1 or i==1):
                matrix[i][j]=b
                b=b+2
    return matrix
n = int(input("Enter the size of the matrix: "))
matrix = [[0 for j in range(n)] for i in range(n)]
matrix1=swajith(matrix)
for i in range(n):
    for j in range(n):
        print("{:2d}".format(matrix1[j][i]), end=" ")
    print()
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
