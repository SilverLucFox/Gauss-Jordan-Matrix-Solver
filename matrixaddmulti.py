import numpy as np

def get_matrix_dimensions(matrix_name):
    while True:
        try:
            rows = int(input(f"Enter number of rows for {matrix_name}: "))
            cols = int(input(f"Enter number of columns for {matrix_name}: "))
            if rows > 0 and cols > 0:
                return rows, cols
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
rows_C, cols_C = get_matrix_dimensions("Matrix C")

if cols_B != rows_A:
    print("\nMatrix multiplication BA is NOT possible. Columns of B must equal rows of A.")
elif cols_A != rows_C:
    print("\nMatrix multiplication AC is NOT possible. Columns of A must equal rows of C.")
else:
    A = get_matrix(rows_A, cols_A, "Matrix A")
    B = get_matrix(rows_B, cols_B, "Matrix B")
    C = get_matrix(rows_C, cols_C, "Matrix C")

    while True:
        try:
            coeff_BA = float(input("Enter the coefficient for BA (default is 3): ") or 3)
            coeff_AC = float(input("Enter the coefficient for AC (default is 4): ") or 4)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    BA = np.dot(B, A)
    AC = np.dot(A, C)

    result = (coeff_BA * BA) + (coeff_AC * AC)

    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nMatrix C:")
    print(C)
    print("\nMatrix BA:")
    print(BA)
    print("\nMatrix AC:")
    print(AC)
    print(f"\nFinal Result ({coeff_BA} * BA + {coeff_AC} * AC):")
    print(result)
