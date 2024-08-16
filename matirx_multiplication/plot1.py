import matplotlib.pyplot as plt

# Example data
sizes = [64, 128, 256, 512, 1024]
# Example data
cpp_sys_time_int = [0.000, 0.001, 0.000, 0.001, 0.001]
cpp_sys_time_double = [0.000, 0.000, 0.000, 0.000, 0.020]
python_sys_time_int = [0.000, 0.000, 0.010, 0.041, 0.340]
python_sys_time_double = [0.001, 0.011, 0.010, 0.010, 0.370]

plt.figure(figsize=(10, 6))
plt.plot(sizes, cpp_sys_time_int, label='C++ INT', marker='o')
plt.plot(sizes, cpp_sys_time_double, label='C++ DOUBLE', marker='o')
plt.plot(sizes, python_sys_time_int, label='Python INT', marker='x')
plt.plot(sizes, python_sys_time_double, label='Python DOUBLE', marker='x')
plt.xlabel('Matrix Size (N)')
plt.ylabel('System Time (CPU) (seconds)')
plt.title('System Time (CPU) vs Matrix Size')
plt.legend()
plt.grid(True)
plt.show()