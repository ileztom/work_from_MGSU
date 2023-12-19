import numpy as np
array_3d = np.empty((4, 4, 4))
for i in range(4):
    for j in range(4):
        for k in range(4):
            value = np.sin(-np.pi + (2 * np.pi / 3) * i)
            array_3d[i, j, k] = value
print("3D массив:")
print(array_3d)
mean_value = np.mean(array_3d)
median_value = np.median(array_3d)
std_deviation = np.std(array_3d)
print("\nСреднее значение:", mean_value)
print("Медиана:", median_value)
print("Стандартное отклонение:", std_deviation)