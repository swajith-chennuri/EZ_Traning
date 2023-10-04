def swajith(matrix,n):
    row, col = n//2,0
    num=1
    while num <= n * n:
        matrix[row][col]=num
        num+=1
        new_row,new_col=(row+1)%n,(col-1)%n
        if matrix[new_row][new_col]:
            col=(col+1)%n
        else:
            row,col=new_row,new_col
    return matrix
n = int(input("Enter the size of the matrix: "))
matrix = [[0 for j in range(n)] for i in range(n)]
matrix1=swajith(matrix,n)
for i in range(n):
    for j in range(n):
        print("{:3d}".format(matrix1[j][i]), end=" ")
    print()