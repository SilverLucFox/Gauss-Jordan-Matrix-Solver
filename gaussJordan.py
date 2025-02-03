import numpy as np

def print_matrix(matrix, step):
    print(f"Step {step}:")
    print(np.array2string(matrix, formatter={'all': lambda x: f'{x: .3f}'}))
    print()

def input_matrix(rows, cols):
    A = []
    b = []
    
    print("\nPlease enter the augmented matrix (with right-hand side in the last column):")
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Enter row {i + 1} (e.g., 'a b c d'): ").split()))
                if len(row) != cols:
                    print(f"Row should contain {cols} elements. Try again.")
                else:
                    A.append(row[:-1])
                    b.append(row[-1])
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only, separated by spaces.")
        
        print("\nCurrent Augmented Matrix:")
        matrix = np.hstack((A, np.array(b).reshape(-1, 1)))
        print_matrix(matrix, i + 1)
    
    return A, b

def gauss_jordan(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    augmented_matrix = np.hstack((A, b))
    rows, cols = augmented_matrix.shape
    step = 1
    
    print("Initial Augmented Matrix:")
    print_matrix(augmented_matrix, step)
    
    for i in range(rows):
        pivot = augmented_matrix[i, i]
        if pivot == 0:
            for j in range(i + 1, rows):
                if augmented_matrix[j, i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    print(f"R{i+1} <-> R{j+1}")
                    print_matrix(augmented_matrix, step)
                    pivot = augmented_matrix[i, i]
                    step += 1
                    break
        
        if pivot == 0:
            print("Matrix is singular and may have infinitely many solutions or no solution.")
            return None
        
        augmented_matrix[i] /= pivot
        print(f"R{i+1} -> R{i+1} / {pivot}")
        print_matrix(augmented_matrix, step)
        step += 1
        
        for j in range(rows):
            if i != j:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]
                print(f"R{j+1} -> R{j+1} - ({factor}) * R{i+1}")
                print_matrix(augmented_matrix, step)
                step += 1
    
    solution = augmented_matrix[:, -1]
    
    if np.allclose(A @ solution, b):
        rank_A = np.linalg.matrix_rank(A)
        rank_augmented = np.linalg.matrix_rank(augmented_matrix)
        if rank_A < rank_augmented:
            print("The system has no solution.")
        elif rank_A == rank_augmented:
            print("The system has infinitely many solutions.")
    
    return solution

if __name__ == "__main__":
    rows = int(input("Enter number of equations: "))
    cols = int(input("Enter number of variables: ")) + 1
    A, b = input_matrix(rows, cols)
    
    solution = gauss_jordan(A, b)
    if solution is not None:
        print("Solution:", solution)
