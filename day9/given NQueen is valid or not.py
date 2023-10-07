def valid_NQueen(matrix):
    a=list(map(int,input().split()))
    b=len(a)-1
    matrix.append(a[:])
    for i in range(b):
        c=list(map(int,input().split()))
        matrix.append(c[:])
    def check_diagonals(row, col):
        # Check upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if matrix[i][j] == 1:
                return False

        # Check upper-right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if matrix[i][j] == 1:
                return False

    for i in range(len(a)):
        if sum(matrix[i])!=1:
            return False
        b=0
        for j in range(len(a)):
            b=b+matrix[j][i]
            if b>1:
                return False
            if matrix[i][j]==1:
                if not check_diagonals(i,j):
                    return False 
    return True
matrix=[]
b=valid_NQueen(matrix)
print(b)