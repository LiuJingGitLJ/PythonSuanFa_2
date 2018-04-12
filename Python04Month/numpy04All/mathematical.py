# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print('求和，求平均')
arr = np.random.randn(5, 4)
print(arr)

print(arr.mean())
print(arr.sum())

print(arr.mean(axis=1)) #对每一行的元素求平均
print(arr.sum(0)) #对每一列的元素求和， axis 可省略


print('consum 和  cumprod 函数演示')
arr = np.array([0, 1, 2], [3, 4, 5], [6, 7, 8])
print(arr.cumsum(0))
print(arr.cumprod(1))
