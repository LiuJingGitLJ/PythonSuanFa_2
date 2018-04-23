# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pylab
'''
利用数组进行数据处理 简介
• NumPy数组使你可以将许多种数据处理任务表述为简洁的数组表达式(否则需 要编写循环)。用数组表达式代替循环的做法，通常被称为矢量化。
• 矢量化数组运算要比等价的纯Python方式快上一两个数量级
'''
points = np.arange(-5, 5, 0.01) # 生成100个点
xs, ys = np.meshgrid(points, points)  # xs, ys互为转置矩阵
print (xs)
print (ys)
z = np.sqrt(xs ** 2 + ys ** 2)
print (z)
# 画图
plt.imshow(z, cmap = plt.cm.gray);
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
pylab.show() 