# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as np_random

print('求平方根')
arr = np.arange(10)
print(arr)
print('sqrt---')
print(np.sqrt(arr))
print('\n')

print('数组比较')
x = np_random.randn(8)
y = np_random.randn(8)
print(x)
print(y)
print(np.maximum(x,y))

print('使用modf函数 把浮点数分解成为整数和小数部分')
arr = np_random.randn(7) * 5

print('用unique 函数去重')
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(sorted(set(names))) #传统的python做法
print(np.unique(names))

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
