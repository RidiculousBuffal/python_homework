# -*- coding: gb2312 -*-
from typing import Any

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

steps = 100  # ���ò���
rand_walk = np.random.choice([-1, 1], size=(2, steps))  # ��һ����x�ڶ�����y,1��ʾ�����ƶ�,-1��ʾ����
print("rand_walk")
print(rand_walk)
print("-------------------------------------")
position = rand_walk.cumsum(axis=1)  # �ۺϺ�����������,��᲻���ۼ�1,-1
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
plt.plot(position[0], position[1], c='g', marker='*')  # ��position�е����ݿ��ӻ�
plt.scatter(0, 0, c='r', marker='o')  # ������ԭ��
plt.text(0.1, -0.1, 'origin')  # ���д������������ͼ���е����� (0.1, -0.1) ��λ�����һ���ı���ǩ����ǩ����Ϊ "origin"��
plt.scatter(position[0][-1], position[1][-1], c='r', marker='o')  # �������յ�
plt.text(position[0][-1] + 0.1, position[1][-1], 'stop')
plt.show()
