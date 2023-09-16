# -*- coding: gb2312 -*-
from typing import Any

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

steps = 100  # 设置步数
rand_walk = np.random.choice([-1, 1], size=(2, steps))  # 第一行是x第二行是y,1表示正向移动,-1表示负向
print("rand_walk")
print(rand_walk)
print("-------------------------------------")
position = rand_walk.cumsum(axis=1)  # 聚合函数计算坐标,其会不断累加1,-1
print("position")
print(position)
print('------------------------------------')
distance = [np.linalg.norm([position[0][i], position[1][i]]) for i in range(len(position[0]))]
distance = np.array(distance)
print('distance')
print(distance)
print('---------------------------')
np.set_printoptions(precision=4)
plt.cla()
plt.plot(position[0], position[1], c='g', marker='*')  # 将position中的数据可视化
plt.scatter(0, 0, c='r', marker='o')  # 单独画原点
plt.text(0.1, -0.1, 'origin')  # 这行代码的作用是在图形中的坐标 (0.1, -0.1) 的位置添加一个文本标签，标签内容为 "origin"。
plt.scatter(position[0][-1], position[1][-1], c='r', marker='o')  # 单独画终点
plt.text(position[0][-1] + 0.1, position[1][-1], 'stop')
plt.show()
