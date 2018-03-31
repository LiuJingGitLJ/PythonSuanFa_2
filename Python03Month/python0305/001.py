# -*- coding: utf-8 -*-
#向量相加-Python

def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    '''
    错误写法
    a = range(n)
    b = range(n)
    TypeError: 'range' object does not support item assignment
    '''
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c

#向量相加-NumPy
import numpy

def numpysum(n):
    a = numpy.arange(n) ** 2
    b = numpy.arange(n) ** 3
    c = a + b
    return c


#效率比较
import sys
from datetime import datetime
import numpy



size = 1000

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start

print('最后两个元素的总和', c[-2:])
print('PythonSum 计算时间毫秒级', delta.microseconds)

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print('最后两个元素的总和', c[-2:])
print('numpysum 计算时间毫秒级', delta.microseconds)


