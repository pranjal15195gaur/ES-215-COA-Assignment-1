import matplotlib.pyplot as plt

# Matrix sizes
matrix_sizes = [64, 128, 256, 512, 1024]

# Meat Time (s) for Python and C++
python_meat_times_double = [0.189808, 1.721142, 13.010997, 106.097571, None]  # None for missing data
python_meat_times_integer = [0.100245, 0.794321, 6.456137, 52.107652, 452.261143]
cpp_meat_times_double = [0.0012716, 0.0100443, 0.083377, 0.803527, 9.00745]
cpp_meat_times_integer = [0.0014586, 0.0099817, 0.0859125, 0.710498, 5.54689]

# Plotting Meat Time vs Matrix Size
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, python_meat_times_double, label='Python Double', marker='x')
plt.plot(matrix_sizes, python_meat_times_integer, label='Python Integer', marker='x')
plt.plot(matrix_sizes, cpp_meat_times_double, label='C++ Double', marker='o')
plt.plot(matrix_sizes, cpp_meat_times_integer, label='C++ Integer', marker='o')
plt.xlabel('Matrix Size (N)')
plt.ylabel('Meat Time (s)')
plt.title('Meat Time vs Matrix Size')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Log scale for better visualization
plt.show()
