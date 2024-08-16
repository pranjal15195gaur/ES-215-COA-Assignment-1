import time
import numpy as np


def matrix_multiply_double(N, matrix1, matrix2):
    result = np.zeros((N, N), dtype=float)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

cpu_start_time = time.time()

N = 512
matrix1d = np.ones((N, N), dtype=float)
matrix2d = np.ones((N, N), dtype=float) * 2.0

meat_start_time = time.time()
matrix_multiply_double(N, matrix1d, matrix2d)
meat_time = time.time() - meat_start_time
print(f"Matrix size: {N}x{N} | Meat time (Double): {meat_time:.6f} seconds")

cpu_time = time.time() - cpu_start_time
print(f"Matrix size: {N}x{N} | CPU Time (Double): {cpu_time:.6f} seconds")

