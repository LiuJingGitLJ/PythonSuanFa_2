import numpy as np

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
