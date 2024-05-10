import numpy as np

def crout_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        for i in range(j, n):
            if i == j:
                L[i, j] = 1
                sum_val = sum(L[i, k] * U[k, j] for k in range(i))
                U[i, j] = A[i, j] - sum_val
            else:
                sum_val = sum(L[i, k] * U[k, j] for k in range(j))
                L[i, j] = (A[i, j] - sum_val) / U[j, j]
        for i in range(j + 1, n):
            sum_val = sum(L[j, k] * U[k, i] for k in range(j))
            U[j, i] = A[j, i] - sum_val

    return L, U

def solve_linear_system(A, b):
    L, U = crout_decomposition(A)

    # Penyelesaian Ly = b (matriks segitiga bawah)
    y = np.linalg.solve(L, b)

    # Penyelesaian Ux = y (matriks segitiga atas)
    x = np.linalg.solve(U, y)

    return x

# Contoh penggunaan
A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], dtype=float)
b = np.array([1, 0, 1], dtype=float)

solution = solve_linear_system(A, b)
print("Solusi sistem persamaan linear:")
for i, sol in enumerate(solution):
    print(f"x{i+1} = {sol}")
