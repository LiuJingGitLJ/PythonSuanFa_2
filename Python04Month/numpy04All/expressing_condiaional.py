# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print('通过真值表选择元素')
x_arr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y_arr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
reslut = [(x if c else y) for x, y, c in zip(x_arr, y_arr, cond)] #通过列表推导实现
print(reslut)
print(np.where(cond, x_arr, y_arr)) #使用numpy Where函数

print('更多的where的例子')
arr = np_random.randn(4, 4)
print(arr)
print(np.where(arr > 0, 2, -2))
print(np.where(arr > 0, 2, arr))

print('where嵌套')
cond_1 = np.array([True, False, True, True, False])
cond_2  = np.array([False, True, False, True, False])

result = []
for i in range(len(cond)):
    if cond_1[i] and cond_2[i]:
        result.append(0)
    elif cond_1[i]:
        result.append(1)
    elif cond_2[i]:
        result.append(2)
    else:
        result.append(3)
print('jieguo ------')
print(result)

result = np.where(cond_1 & cond_2, 0, np.where(cond_1, 1, np.where(cond_1, 1, np.where(cond_2, 2, 3))))
print(result)


