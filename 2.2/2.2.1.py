# -*- coding: gb2312 -*-
from typing import Any
import pandas as pd
import numpy as np
import inspect


def deb(arr):
    frame = inspect.currentframe().f_back
    code = frame.f_code
    arg_name = inspect.getframeinfo(frame).code_context[0].split('(')[1].split(')')[0].split('=')[0].strip()
    print(arg_name + ':')  # t����,��ӡ����ֵ
    print(arr)


# ����,�ֶ���,�õ�,ũ����4����������ƻ��,��,�㽶,���Ӻ�â��5��ˮ��,ʹ��numpy��ndarrayʵ�����¹���
# ����һά����ֱ𴢴泬�к�ˮ��������
shop = np.array(['����', '�ֶ���', '�õ�', 'ũ����'])
deb(shop)
fruit = np.array(['ƻ��', '��', '�㽶', '����', 'â��'])
deb(fruit)
# ����һ��4*5�Ķ�ά����,�ֱ𴢴�۸�,���м۸���4-10Ԫ֮��
price = np.random.uniform(4, 10, size=(4, 5))
deb(price)
# ѡ����󷢵�ƻ���ͺõµ��㽶,�����۸�����һԪ
##��ѡ����󷢵�ƻ��,�����1
# var1 = price[shop == '����'][:, fruit == 'ƻ��'] + 1
# var2 = price[shop == '�õ�'][:, fruit == '�㽶'] + 1
# var1 = var1[0][0]
# var2 = var2[0][0]
price[np.where(shop == '����')[0][0]][np.where(fruit == 'ƻ��')[0][0]] += 1
price[np.where(shop == '�õ�')[0][0]][np.where(fruit == '�㽶')[0][0]] += 1
# np.where���ص���һ��Ԫ��(array([?], dtype=int64),) ������shop��fruit����һά��,��ֻ��һ��Ԫ��
# ��np.where()[0]ȡ���õ�����һ���б�,�б�����һ��Ԫ����Ѱ�ҵ�Ԫ���ڶ�Ӧarray�е�λ��
# np.where()[0][0]�ǽ��б��еĵ�һ��Ԫ��ȡ��,Ҳ�����������±�
print('-----------new price------------')
print(price)
print('---------------')
# ũ���̵�ˮ�������,�����е�ˮ���۸����2Ԫ
price[np.where(shop == 'ũ����')[0][0]] -= 2
print('-----------new price------------')
print(price)
print('---------------')
# ͳ��4������ƻ����â�������۾���
means = price[:, (fruit == 'ƻ��') | (fruit == 'â��')].mean(axis=0)
##��ѡ��ȫ��������  �ո�:�ո� ������ʾ,���пո����ʡ�����оͱ����: �������
print(means)
# �ҳ����Ӽ۸����ĳ�������
name = shop[price[:, (fruit == '����')].argmax()]
print(name)
