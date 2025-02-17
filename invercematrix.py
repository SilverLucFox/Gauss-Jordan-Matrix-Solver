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

def inverse_matrix(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return "This matrix is singular and cannot be inverted."

rows_A, cols_A = get_matrix_dimensions("Matrix A")

A = get_matrix(rows_A, cols_A, "Matrix A")

inverse_A = inverse_matrix(A)

print("\nMatrix A:")
print(A)
print("\nInverse of Matrix A:")
print(inverse_A)

# Calculate the identity matrix result
identity_result = np.dot(inverse_A, A)

# Displaying the identity matrix (M^-1 * M)
print("\nMatrix M^-1 * M (Resulting Identity Matrix):")
print(identity_result)

# Accessing the diagonal values (which should be 1s for the identity matrix)
for i in range(min(identity_result.shape[0], identity_result.shape[1])):
    formula = f"M^-1 * M[{i+1},{i+1}] = {identity_result[i, i]}"
    print(f"Formula for {i+1}th row, {i+1}th column: {formula}")
    print(f"Value at row {i+1}, column {i+1}: {identity_result[i, i]}")
