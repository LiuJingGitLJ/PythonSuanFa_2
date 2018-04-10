# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as np_random

print('Repeat:按元素')
arr = np.arange(3)
print(arr)
print('\n')
print(arr.repeat(3))
print(arr.repeat([2, 3, 4]))#3个元素，分别复制2 3 4次 长度要匹配

print('Repeat, 指定轴')
arr = np_random.randn(2, 2)
print(arr)
print('\n')
print(('按行重复'))
print(arr.repeat(3, axis=0)) #按行repeat
print('按列重复')
print(arr.repeat(2, axis=1)) #按列repeat
print(('按行重复'))
print(arr.repeat(3, axis=0)) #按行repeat

print('Tile：参考贴瓷砖')
print(np.tile(arr, 2))
print('np.title(arr,(2, 3)')
print(np.tile(arr, (2, 3)))