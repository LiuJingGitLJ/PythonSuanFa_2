# -*- coding:utf-8 -*-

import numpy as np

print('使用普通一维数组生成bumpy一维数组')
data = [2, 4, 8.7, 5, 9]
arr = np.array(data)
print(arr)

print('打印元素类型')

print(arr.dtype)
print('\n')

#使用普通二维数组生成numpy二维数组

data2 = [[1, 2, 3, 4],[5, 6, 4, 2]]
arr2 = np.array(data2)
print(arr2)

print('打印数组长度')
print(arr2.shape)

print('\n')



