import numpy as np
array_3d = np.empty((4, 4, 4))
for i in range(4):
    for j in range(4):
        for k in range(4):
            value = np.sin(-np.pi + (2 * np.pi / 3) * i)
            array_3d[i, j, k] = value
print(array_3d)
