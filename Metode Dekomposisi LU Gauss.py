import numpy as np

def lu_gauss_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        U[j, j] = 1
        for i in range(j, n):
            sum_val = sum(L[i, k] * U[k, j] for k in range(i))
            L[i, j] = A[i, j] - sum_val
        for i in range(j, n):
            sum_val = sum(L[j, k] * U[k, i] for k in range(j))
            U[j, i] = (A[j, i] - sum_val) / L[j, j]

    return L, U

def solve_linear_system(A, b):
    L, U = lu_gauss_decomposition(A)

    # Penyelesaian Ly = b
    y = np.linalg.solve(L, b)

    # Penyelesaian Ux = y
    x = np.linalg.solve(U, y)

    return x

# Contoh penggunaan
A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])

solution = solve_linear_system(A, b)
print("Solusi sistem persamaan linear:")
for i, sol in enumerate(solution):
    print(f"x{i+1} = {sol}")
