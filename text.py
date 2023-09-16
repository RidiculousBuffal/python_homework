import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# 找到元素5的坐标
index = np.where(arr == 2)

print(index[0])
