import numpy

m = numpy.mat([[1, 2], [3, 4]])
print("Matrix.Transpose:")
print(m.T)

a = numpy.mat([1, 2])
b = numpy.mat([[10], [20]])
print(a * b)
print(a.T * b.T)

a = numpy.mat([[1, 2], [3, 4]])
b = numpy.mat([[10, 20], [30, 40]])
print(a * b)

x = numpy.array([1, 2])
y = numpy.array([10, 20])
print("Array inner:")
print(numpy.inner(x, y))
''' Output：
Array inner:
50
'''

x = numpy.mat([[1, 2], [3, 4]])
y = numpy.mat([10, 20])
print("Matrix inner:")
print(numpy.inner(x, y))
''' Output：
Matrix inner:
[[ 50]
 [110]]
'''