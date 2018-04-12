# -*- coding: utf-8 -*-
import numpy as np


print('数组文件读写')
arr = np.arange(10)
np.save('some_array', arr)
print(np.load('some_array.npy'))

print('多个数组压缩存储')
np.savez('array_archive.npz', a = arr, b = arr)
arch = np.load('array_archive.npz')

print('使用列表生成一维数组')
data = [1, 2, 3, 4, 5]
x = np.array(data)
print(x)#打印数组
print(x.dtype)#打印数组的类型

print('使用列表生成二维数组')
data = [[1, 2], [3, 4], [5, 6]]
x = np.array(data)

print(x)#打印数组
print(x.ndim)#打印数组的维度
print(x.shape)#打印数组各个维度的长度，shape是一个元组

print('使用zero/ones/empty创建数组，根据shape来创建')
x = np.zeros(6) #创建一维长度为6的，元素都是0的一维数组
print(x)

x = np.zeros((2, 3)) #创建一维长度为2，二维长度为3的二维0数组
print(x)

x = np.ones((2, 3)) #创建一维长度为2，二维长度为3的二维1数组
print(x)

x = np.empty((2, 3))#创建一维长度为2，二维长度为3 未初始化的二维数组
print(x)

print('使用arrange生成连续元素')
print(np.arange(6))
#起始点 结束点 步长 （步长 即从起始点 每隔几个数 前进几步）
print(np.arange(0, 6, 1))

print('arange 和 reshape的混合使用')
a = np.arange(6).reshape(2, 3)  #2行3列 tuple类型
print(a)
# print(np.arange.__doc__) 打印文档

print('循环使用 range(0, 5)')
c = [i for i in range(0, 5)] #从0 开始到4，不包括5，默认的间隔为1
print(c)

'''
range()函数

    函数说明： range(start, stop[, step]) -> range object，根据start与stop指定的范围以及step设定的步长，生成一个序列。
    参数含义：start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
                  end:技术到end结束，但不包括end.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
                  scan：每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
    函数返回的是一个range object
    例子：

小记： #range中的setp 不能使float  
'''
#
c = [i for i in range(0, 5)] #从0开始 到4  开区间 默认间隔2


'''
arrange()函数

    函数说明：arange([start,] stop[, step,], dtype=None)根据start与stop指定的范围以及step设定的步长，生成一个 ndarray。 dtype : dtype
            The type of the output array.  If `dtype` is not given, infer the data
            type from the other input arguments.
            
'''
print(np.arange(3))

print('np.arange(3.0)')
print(np.arange(3.0))

print('np.arange(3, 7)')
print(np.arange(3, 7))

print(np.arange(3, 7, 2))

















