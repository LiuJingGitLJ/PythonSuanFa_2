import numpy as np
import numpy.random as np_random
a = np.array([1,  2,  3,4,5], ndmin =  2)
print (a)
#ndarray 对象由计算机内存中的一维连续区域组成，带有将每个元素映射到内存块中某个位置的索引方案。
# 内存块以按行(C 风格)或按列(FORTRAN 或 MatLab 风格)的方式保存元素。
a2 = np.array([1,  2,  3], dtype = complex)
print (a2)

a3 = np.array([[1,2,3],[4,5,6]])
print (a3.shape)

'''
ndarray.shape
这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。
'''
a4 = np.array([[1,2,3],[4,5,6]])
a4.shape =  (3,2)
print(a4)

a5 = np.array([[1,2,3],[4,5,6]])
b5 = a5.reshape(3,2)
print (b5)
print(b5.ndim)

a6 = np.arange(24)
print (a6)
print(a6.ndim)

print('连接两个二维数组')

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate([arr1, arr2], axis=0))
print(np.concatenate([arr1, arr2], axis=1))

# 所谓堆叠 是连接的另外一种描述
print('垂直stack 与 水平 stack')
print(np.vstack((arr1, arr2)))#垂直堆叠
print(np.hstack((arr1, arr2)))#水平堆叠
print('nnn')

print('拆分数组')
arr = np_random.randn(5, 5)
print(arr)
print('水平拆分')

first, second, third = np.split(arr, [1, 3], axis=0)
print(first)
print(second)
print(third)

print('垂直拆分')

#堆叠辅助类
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np_random.randn(3, 2)
#r_用于按行堆叠
print(np.r_[arr1,arr2])
print(np.c_[np.r_[arr1, arr2], arr])
print(np.c_[np.r_[arr1, arr2], arr])
#切片直接转换为数组
print(np.c_[1:6, -10:-5])

arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np_random.randn(3, 2)
#r_用户按行堆叠
print(np.r_[arr1, arr2])
print(np.c_[np.r_[arr1, arr2], arr])
print(np.c_[np.r_[arr1, arr2], arr])
#切片直接转换为数组

print(np.c_[1:6, -10:-5])




