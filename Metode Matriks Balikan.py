import numpy as np

def solve_linear_system(A, b):
    # Mencari matriks balikan dari A
    A_inv = np.linalg.inv(A)
    
    # Mengalikan matriks balikan A dengan vektor b
    x = np.dot(A_inv, b)
    
    return x

# Contoh penggunaan
A = np.array([[2, 3], [1, -1]])
b = np.array([8, -1])

solution = solve_linear_system(A, b)
print("Solusi sistem persamaan linear:")
for i, sol in enumerate(solution):
    print(f"x{i+1} = {sol}")
