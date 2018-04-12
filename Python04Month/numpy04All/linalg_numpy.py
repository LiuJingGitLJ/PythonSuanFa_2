# -*- coding: utf-8 -*-

import numpy as np
import numpy.linalg as nla

print('numpy 线性代数')
print('矩阵点乘')

x = np.array([[1, 2], [3, 4]])
y = np.array([[1, 3], [2, 4]])
print('x.dot(y):')
print(x.dot(y))
print('----y.dot(x):')
print(y.dot(x))

print('np.dot(x,y):')
print(np.dot(x, y))
print('np.dot(y,x):')
print(np.dot(y, x))

print('\n矩阵求逆:\n')
x = np.array([[1, 1], [1, 2]])
y = nla.inv(x) #矩阵求逆（若矩阵的逆存在）

print('nla.inv 单位的逆矩阵')
print(x.dot(y)) #单位矩阵[[1. 0.]]
#求行列式
print(nla.det(x))