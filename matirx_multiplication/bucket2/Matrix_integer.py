import time
import numpy as np

def matrix_multiply(N, matrix1, matrix2):
    result = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


cpu_start_time = time.time()

N = 1024

matrix1 = np.ones((N, N), dtype=int)
matrix2 = np.ones((N, N), dtype=int) * 2

meat_start_time = time.time()
matrix_multiply(N, matrix1, matrix2)
meat_time = time.time() - meat_start_time
print(f"Matrix size: {N}x{N} | Meat time (Integer): {meat_time:.6f} seconds")

cpu_time = time.time() - cpu_start_time
print(f"Matrix size: {N}x{N} | CPU Time (Integer): {cpu_time:.6f} seconds")


