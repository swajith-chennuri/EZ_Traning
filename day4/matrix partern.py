# Get size of the matrix from user
n = int(input("Enter the size of the matrix: "))
# Initialize the matrix with zeros
matrix = [[0 for j in range(n)] for i in range(n)]
# Define variables for the starting and ending indices of the current spiral
start_row, end_row = 0, n-1
start_col, end_col = 0, n-1
# Initialize the counter variable to 1
count = 1
# Loop through the matrix in a spiral pattern and assign values
while start_row <= end_row and start_col <= end_col:
    # Assign values to the top row
    for i in range(start_col, end_col+1):
        matrix[start_row][i] = count
        count += 1
    # Assign values to the right column
    for i in range(start_row+1, end_row+1):
        matrix[i][end_col] = count
        count += 1   
    # Assign values to the bottom row
    for i in range(end_col-1, start_col-1, -1):
        matrix[end_row][i] = count
        count += 1 
    # Assign values to the left column
    for i in range(end_row-1, start_row, -1):
        matrix[i][start_col] = count
        count += 1
    # Update the indices for the next spiral
    start_row += 1
    end_row -= 1
    start_col += 1
    end_col -= 1
# Print the matrix in the specified format
for i in range(n):
    for j in range(n):
        print("{:2d}".format(matrix[i][j]), end=" ")
    print()
