import numpy as np
array_3d = np.empty((4, 4, 4))
for i in range(4):
    for j in range(4):
        for k in range(4):
            value = np.sin(-np.pi + (2 * np.pi / 3) * i)
            array_3d[i, j, k] = value
print("3D массив:")
print(array_3d)
slice_2d_1 = array_3d[:, :, 2]
slice_2d_2 = array_3d[1, :, :]
print("\n2D срез 1:")
print(slice_2d_1)
print("\n2D срез 2:")
print(slice_2d_2)
sum_slice_1 = np.sum(slice_2d_1)
mean_slice_2 = np.mean(slice_2d_2)
print("\nСумма элементов в 2D срезе 1:", sum_slice_1)
print("Среднее значение в 2D срезе 2:", mean_slice_2)
