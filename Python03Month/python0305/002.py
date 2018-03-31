# -*- coding: utf-8 -*-

# numpy简介

import sys
import numpy

a = numpy.arange(5)
print('a.type = ', a.dtype)

a
a.shape

#创建多维数组
m = numpy.array([numpy.arange(2), numpy.arange(2)])

print('多维数组m = ', m)
#数组的维度
print('m.shape = ', m.shape)
print('m.dtype = ', m.dtype)

numpy.zeros(10)
numpy.zeros((3, 6))
numpy.empty((2, 3, 2))
numpy.arange(15)

#选取数组元素
a = numpy.array([[1, 2], [3, 4]])
print("In: a", a)

print("In: a[0,0]", a[0, 0])

print("In: a[0,1]", a[0, 1])
print("In: a[1, 0]", a[1, 0])


