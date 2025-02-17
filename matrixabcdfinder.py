import numpy as np

def display_matrix(matrix, name):
    print(f"\n{name}:")
    for row in matrix:
        print(row)

def get_matrix(rows, cols, name):
    matrix = [[None] * cols for _ in range(rows)]
    i, j = 0, 0

    while i < rows:
        while j < cols:
            display_matrix(matrix, name)
            value = input(f"Enter value for {name}[{i+1}][{j+1}] (or type 'back' to go back): ")
            
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

A = get_matrix(2, 2, "Matrix A")
X = get_matrix(2, 2, "Matrix X (unknown matrix)")
B = get_matrix(2, 2, "Matrix B")

if A.shape[1] != X.shape[0]:
    print("\nMultiplication AX is NOT possible. Columns of A must equal rows of X.")
else:
    equations = np.dot(A, X)
    
    print("\nSolving for unknowns...")
    variables = ['a', 'b', 'c', 'd']
    solutions = {}

    for i in range(2):
        for j in range(2):
            eq = equations[i][j]
            expected = B[i][j]
            solutions[variables[i * 2 + j]] = expected

    print("\nSolution:")
    for var, value in solutions.items():
        print(f"{var} = {value}")

    result_X = np.array([[solutions['a'], solutions['b']], [solutions['c'], solutions['d']]])
    print("\nSolved Matrix X:")
    print(result_X)
