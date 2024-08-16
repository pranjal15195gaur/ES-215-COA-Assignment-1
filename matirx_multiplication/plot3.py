import matplotlib.pyplot as plt

# Matrix sizes
matrix_sizes = [64, 128, 256, 512, 1024]

# CPU Time (s) for Python and C++
python_cpu_times_double = [0.189808, 1.729271, 13.010997, 106.108330, None]  # None for missing data
python_cpu_times_integer = [0.100245, 0.794978, 6.458064, 52.107652, 452.263142]
cpp_cpu_times_double = [0.0026933, 0.0118306, 0.0853749, 0.80683, 9.01652]
cpp_cpu_times_integer = [0.0029301, 0.0116263, 0.0876725, 0.713184, 5.55229]

# Plotting CPU Time vs Matrix Size
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, python_cpu_times_double, label='Python Double', marker='x')
plt.plot(matrix_sizes, python_cpu_times_integer, label='Python Integer', marker='x')
plt.plot(matrix_sizes, cpp_cpu_times_double, label='C++ Double', marker='o')
plt.plot(matrix_sizes, cpp_cpu_times_integer, label='C++ Integer', marker='o')
plt.xlabel('Matrix Size (N)')
plt.ylabel('CPU Time (s)')
plt.title('CPU Time vs Matrix Size')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Log scale for better visualization
plt.show()
