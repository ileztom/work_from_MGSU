import numpy as np
array_3d = np.empty((4, 4, 4))
for i in range(4):
    for j in range(4):
        for k in range(4):
            value = np.sin(-np.pi + (2 * np.pi / 3) * i)
            array_3d[i, j, k] = value
print("3D массив:")
print(array_3d)
sum_multiple_of_three = np.sum(array_3d[array_3d % 3 == 0])
print("\nСумма элементов, кратных трём:", sum_multiple_of_three)