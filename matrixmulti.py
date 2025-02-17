import numpy as np

def get_matrix_dimensions(matrix_name):
    while True:
        try:
            rows = int(input(f"Enter number of rows for {matrix_name}: "))
            cols = int(input(f"Enter number of columns for {matrix_name}: "))
            if rows > 0 and cols > 0:
                return rows, cols
            else:
                print("Rows and columns must be positive integers.")
        except ValueError:
            print("Invalid input. Please enter integers.")

def display_matrix(matrix, matrix_name):
    print(f"\nCurrent state of {matrix_name}:")
    for row in matrix:
        print(row)

def get_matrix(rows, cols, matrix_name):
    matrix = [[None] * cols for _ in range(rows)]
    i, j = 0, 0

    while i < rows:
        while j < cols:
            display_matrix(matrix, matrix_name)
            value = input(f"Enter value for {matrix_name}[{i+1}][{j+1}] (or type 'back' to go back): ")
            
            if value.lower() == "back":
                if j > 0:
                    j -= 1
                elif i > 0:
                    i -= 1
                    j = cols - 1
                else:
                    print("Already at the beginning.")
                continue

            try:
                matrix[i][j] = float(value)
                j += 1
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        i += 1
        j = 0

    return np.array(matrix)

rows_A, cols_A = get_matrix_dimensions("Matrix A")
rows_B, cols_B = get_matrix_dimensions("Matrix B")

if cols_A != rows_B:
    print("\nMatrix multiplication is NOT possible. Columns of A must equal rows of B.")
else:
    A = get_matrix(rows_A, cols_A, "Matrix A")
    B = get_matrix(rows_B, cols_B, "Matrix B")

    C = np.dot(A, B)

    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nResultant Matrix C (A × B):")
    print(C)
