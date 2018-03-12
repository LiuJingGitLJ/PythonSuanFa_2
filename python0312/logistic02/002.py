import numpy as np

a = np.array([1, 2, 3], dtype=int)  # 创建1*3维数组   array([1,2,3])
print(type(a))  # numpy.ndarray类型
print(a.shape)  # 维数信息(3L,)
print(a.dtype.name)  # 'int32'
print(a.size)  # 元素个数：3
print(a.itemsize)  # 每个元素所占用的字节数目:4

b = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)  # 创建2*3维数组  array([[1,2,3],[4,5,6]])
print(b.shape)  # 维数信息（2L,3L）
print(b.size)  # 元素个数：6
print(b.itemsize)  # 每个元素所占用的字节数目:4

c = np.array([[1, 2, 3], [4, 5, 6]], dtype='int16')  # 创建2*3维数组  array([[1,2,3],[4,5,6]],dtype=int16)
print(c.shape)  # 维数信息（2L,3L）
print(c.size)  # 元素个数：6
print(c.itemsize)  # 每个元素所占用的字节数目:2
print(c.ndim)  # 维数

d = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex)  # 复数二维数组
print(d.itemsize)  # 每个元素所占用的字节数目：16
print(d.dtype.name)  # 元素类型：'complex128'
print(d.shape)