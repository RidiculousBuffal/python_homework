# -*- coding: gb2312 -*-
import matplotlib.pyplot as plt
import numpy as np
import warnings
# ����matplotlib���о���
warnings.filterwarnings("ignore")
from mpl_toolkits import mplot3d
#matplotlib �������
plt.rcParams["font.sans-serif"] = ["KaiTi"]
plt.rcParams["axes.unicode_minus"] = False

# ����һ��3*10�Ķ�ά����,��¼ÿһ���������������ƶ��ľ���,��ÿ���������ƶ��ľ�����ӱ�׼��̬�ֲ�(����Ϊ0,����Ϊ1)
# ����Ϊ0,1,2�ֱ��Ӧx,y,z��

rand_walk = np.random.normal(0, 1, size=(3, 60))  # �������
print("rand_walk")
print(rand_walk)
print("---------------")
position = rand_walk.cumsum(axis=1)  # λ��
print('positon')
print(position)
print('-----------------')
distance = np.sqrt(rand_walk[0] ** 2 + rand_walk[1] ** 2 + rand_walk[2] ** 2)  # ����
np.set_printoptions(precision=2)
print('distance')
print(distance)
print('---------------')
# z����Զ:
print("the max distance of Z is:", end=' ')
print(np.abs(position[2]).max())
#�������ֵ
print('the min distance of all is ', end=' ')
print(distance.min())
print('----------------ploting------------')
#--------------------------3D��ͼ----------------------------
fig = plt.figure  # ������ͼ����
ax = plt.axes(projection='3d')
ax.plot3D(position[0], position[1], position[2], 'red', linestyle='--')
sc = ax.scatter3D(position[0], position[1], position[2], c=distance, cmap='viridis', linewidths=10)
ax.text3D(position[0][-1], position[1][-1], position[2][-1], 'stop')
cbar = plt.colorbar(sc)
cbar.set_label('����ԭ��ľ���',fontsize=20)
ax.w_xaxis.set_pane_color('#deeaf6')
ax.w_zaxis.set_pane_color('#deeaf6')
ax.w_yaxis.set_pane_color('#deeaf6')
# ���� XYZ�����������Ϊ����
ax.xaxis._axinfo['grid']['linestyle'] = '--'
ax.yaxis._axinfo['grid']['linestyle'] = '--'
ax.zaxis._axinfo['grid']['linestyle'] = '--'
ax.set_title('���߹켣',fontsize=20)
plt.show()
